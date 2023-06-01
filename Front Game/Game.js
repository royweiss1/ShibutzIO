


var slider = document.getElementById("mySlider");

slider.addEventListener("input", function() {
    var value = slider.value;
    document.getElementById("sliderValue").textContent = "Speed: " + value;
  });

slider.value = 1500;
const jsonExample = {
    "1": {
        "(1,0)": "(1,1)",
    },
    "2": {
        "(1,0)": "(1,2)",
        "(2,0)": "(1,1)"
    },
    "3": {
        "(2,0)": "(1,2)",
        "(3,0)": "(1,1)"
    },
    "4": {
        "(3,0)": "(1,2)",
        "(4,0)": "(1,1)",
        "(2,0)": "(1,4)"
    },
    "5": {
        "(4,0)": "(1,2)",
        "(5,0)": "(1,1)"
    },
    "6": {
        "(5,0)": "(1,2)",
        "(6,0)": "(1,1)"
    },
    "7": {
        "(6,0)": "(1,2)",
        "(7,0)": "(1,1)"
    },
    "8": {
        "(7,0)": "(1,2)",
        "(8,0)": "(1,1)"
    },


}

var botList = document.getElementById("botList");
var botItems = botList.getElementsByTagName("li");
var indexMap = new Map();
var currentIndex = 1;

for (var i = 0; i < botItems.length; i++) {
  botItems[i].addEventListener("click", function() {
    if (!indexMap.has(this) && currentIndex <= 3) {
      var index = currentIndex;
      indexMap.set(this, index);
      this.textContent = this.textContent + " " + index;
      currentIndex++;
    }
  });
}

var blockSize = 30;
var rows = 30;
var cols = 30;
var board;
var context;


window.onload = function() {
    board = document.getElementById("canvas");
    context = board.getContext("2d");
    board.width = blockSize * rows;
    board.height = blockSize * cols;

    InitBoard();
    // var img = new Image();
    // img.src = "Art/mario.png";
    // img.onload = function() {
    //     context.drawImage(img, 0, 0, 100, 100);
    // }
    update();
}



async function update() {
    const turns = JSON.parse(JSON.stringify(jsonExample));
    // for each turn
    for (var turn in turns) {
        for(var change in turns[turn]){
            switch(turns[turn][change])
            {
                case "(1,1)":
                    src = "Art/BlueHead.png";
                    break;
                case "(1,2)":
                    src = "Art/BlueTail.png";
                    break;
                case "(1,3)":
                    src = "Art/BlueTile.png";
                    break;
                case "(1,4)":
                    src = "Art/BlueKey.png";
                    break;
                case "(2,1)": // same as above but red
                    src = "Art/RedHead.png";
                    break;
                case "(2,2)":
                    src = "Art/RedTail.png";
                    break;
                case "(2,3)":
                    src = "Art/RedTile.png";
                    break;
                case "(2,4)":
                    src = "Art/RedKey.png";
                    break;
                case "(3,1)": // same as above but black
                    src = "Art/BlackHead.png";
                    break;
                case "(3,2)":   
                    src = "Art/BlackTail.png";
                    break;
                case "(3,3)":
                    src = "Art/BlackTile.png";
                    break;
                case "(3,4)":
                    src = "Art/BlackKey.png";
                    break;
                case "(4,1)": // same as above but white
                    src = "Art/WhiteHead.png";
                    break;
                case "(4,2)":
                    src = "Art/WhiteTail.png";
                    break;
                case "(4,3)":
                    src = "Art/WhiteTile.png";
                    break;
                case "(4,4)":
                    src = "Art/WhiteKey.png";
                    break;
                default:
            }
            change = change.substring(1, change.length-1).split(",");
            change[0] = parseInt(change[0]);
            change[1] = parseInt(change[1]);
            drawTile(src, change[0]*blockSize, change[1]*blockSize);
        }
        await sleep(slider.value);
    }
    
}


function InitBoard() {
    src = "Art/DefaultTile.png";
    for (var i = 0; i < rows; i++) {
        for (var j = 0; j < cols; j++){
            drawTile(src, i*blockSize, j*blockSize);
        }
    }
    src = "Art/BlueTile.png";
    drawTile(src, 0, 0);
    src = "Art/BlueGate.png";
    drawTile(src, 0, 0);
    src = "Art/RedTile.png";
    drawTile(src, blockSize*(rows-1), blockSize*(cols-1));
    src = "Art/RedGate.png";
    drawTile(src, blockSize*(rows-1), blockSize*(cols-1));
    src = "Art/BlackTile.png";
    drawTile(src, 0, blockSize*(cols-1));
    src = "Art/BlackGate.png";
    drawTile(src, 0, blockSize*(cols-1));
    src = "Art/WhiteTile.png";
    drawTile(src, blockSize*(rows-1), 0);
    src = "Art/WhiteGate.png";
    drawTile(src, blockSize*(rows-1), 0);
}
function concurTile(img, x, y){
    src = "Art/DefaultTile.png";
    drawTile(src, x, y);
    drawTile(img, x, y);
}

function drawTile(src, x, y){
    // show image on canvas
    var img = new Image();
    img.src = src;
    img.onload = function() {
        context.drawImage(img, x, y, blockSize, blockSize);
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }