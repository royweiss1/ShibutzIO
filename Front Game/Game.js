


var slider = document.getElementById("mySlider");

slider.addEventListener("input", function() {
    var value = slider.value;
    document.getElementById("sliderValue").textContent = "Speed: " + value;
  });


// var input = [{
//     "turnIndex": 1,
//     "Score": {"0": 1, "1": 2, "2": 3, "3": 4},
//     "SquareChanges": [{"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 3}, {"xPosition": 2, "yPosition": 2, "playerIndex": 0, "Status": 3}, {"xPosition": 3, "yPosition": 3, "playerIndex": 1, "Status": 3}, {"xPosition": 4, "yPosition": 4, "playerIndex": 1, "Status": 3}, {"xPosition": 5, "yPosition": 5, "playerIndex": 0, "Status": 2}, {"xPosition": 6, "yPosition": 6, "playerIndex": 0, "Status": 2}, {"xPosition": 7, "yPosition": 7, "playerIndex": 1, "Status": 2}, {"xPosition": 8, "yPosition": 8, "playerIndex": 1, "Status": 2}, {"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 1}, {"xPosition": 2, "yPosition": 2, "playerIndex": 1, "Status": 1}, {"xPosition": 3, "yPosition": 3, "playerIndex": 2, "Status": 1}, {"xPosition": 4, "yPosition": 4, "playerIndex": 3, "Status": 1}]
// },
//     {"turnIndex": 2, "Score": {"0": 1, "1": 2, "2": 3, "3": 4}, "SquareChanges": [{"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 3}, {"xPosition": 2, "yPosition": 2, "playerIndex": 0, "Status": 3}, {"xPosition": 3, "yPosition": 3, "playerIndex": 1, "Status": 3}, {"xPosition": 4, "yPosition": 4, "playerIndex": 1, "Status": 3}, {"xPosition": 5, "yPosition": 5, "playerIndex": 0, "Status": 2}, {"xPosition": 6, "yPosition": 6, "playerIndex": 0, "Status": 2}, {"xPosition": 7, "yPosition": 7, "playerIndex": 1, "Status": 2}, {"xPosition": 8, "yPosition": 8, "playerIndex": 1, "Status": 2}, {"xPosition": 1, "yPosition": 1, "playerIndex": 0, "Status": 1}, {"xPosition": 2, "yPosition": 2, "playerIndex": 1, "Status": 1}, {"xPosition": 3, "yPosition": 3, "playerIndex": 2, "Status": 1}, {"xPosition": 4, "yPosition": 4, "playerIndex": 3, "Status": 1}]
//     }
// ]

var input;

async function getJson() {
    const response = await fetch('http://127.0.0.1:5500/Front%20Game/try.json').then(response => response.json()).then(data => {
        console.log(data);
        input = data;
    });
}


slider.value = 0;
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

// get the h1 header and change its text
var header = document.getElementById("h1");
header.textContent = "Player1 Vs";

for (var i = 0; i < botItems.length; i++) {
  botItems[i].addEventListener("click", function() {
    if (!indexMap.has(this) && currentIndex <= 3) {
      var index = currentIndex;
      indexMap.set(this, index);
      header.textContent = header.textContent + " " + this.textContent;
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


window.onload = async function() {
    await getJson();
    board = document.getElementById("canvas");
    context = board.getContext("2d");
    board.width = blockSize * rows;
    board.height = blockSize * cols;
    InitBoard();
    while (currentIndex <= 3) {
        await sleep(100);
    }
    update();
}



async function update() {


    for(var turn in input){
        for (var i in input[turn].Score){
            // change text of "blueScore" in html to the score of player 1
            document.getElementById("blueScore").textContent = "Blue: " +   input[turn].Score[0];
            document.getElementById("redScore").textContent = "Red: " +   input[turn].Score[1];
            document.getElementById("blackScore").textContent = "Black: " +   input[turn].Score[2];
            document.getElementById("whiteScore").textContent = "White: " +   input[turn].Score[3];
        }
        for (var change in input[turn].SquareChanges){
            var x = input[turn].SquareChanges[change].xPosition;
            var y = input[turn].SquareChanges[change].yPosition;
            var playerIndex = input[turn].SquareChanges[change].playerIndex;
            var status = input[turn].SquareChanges[change].Status;
            console.log(x,y,playerIndex,status);
            switch((playerIndex,status)){
                case(0,0):
                    src = "Art/DefaultTile.png";
                case (1,1):
                    src = "Art/BlueHead.png";
                    break;
                case (1,2):
                    src = "Art/BlueTail.png";
                    break;
                case (1,3):
                    src = "Art/BlueTile.png";
                    break;
                case (1,4):
                    src = "Art/BlueKey.png";
                    break;
                case (2,1): // same as above but red
                    src = "Art/RedHead.png";    
                    break;
                case (2,2):
                    src = "Art/RedTail.png";
                    break;
                case (2,3):
                    src = "Art/RedTile.png";
                    break;
                case (2,4):
                    src = "Art/RedKey.png";
                    break;
                case (3,1): // same as above but black
                    src = "Art/BlackHead.png";
                    break;
                case (3,2):
                    src = "Art/BlackTail.png";
                    break;
                case (3,3):
                    src = "Art/BlackTile.png";
                    break;
                case (3,4):
                    src = "Art/BlackKey.png";
                    break;
                case (4,1): // same as above but white
                    src = "Art/WhiteHead.png";
                    break;
                case (4,2):
                    src = "Art/WhiteTail.png";
                    break;
                case (4,3):
                    src = "Art/WhiteTile.png";
                    break;
                case (4,4):
                    src = "Art/WhiteKey.png";
                    break;
            }
            console.log(src);
            change = change.substring(1, change.length-1).split(",");
            change[0] = parseInt(change[0]);
            change[1] = parseInt(change[1]);
            drawTile(src, x*blockSize, y*blockSize);
         }
            await sleep(1500-slider.value);
        }
    // const turns = JSON.parse(JSON.stringify(jsonExample));
    // for (var turn in turns) {
    //     for(var change in turns[turn]){
    //         switch(turns[turn][change])
    //         {
    //             case "(1,1)":
    //                 src = "Art/BlueHead.png";
    //                 break;
    //             case "(1,2)":
    //                 src = "Art/BlueTail.png";
    //                 break;
    //             case "(1,3)":
    //                 src = "Art/BlueTile.png";
    //                 break;
    //             case "(1,4)":
    //                 src = "Art/BlueKey.png";
    //                 break;
    //             case "(2,1)": // same as above but red
    //                 src = "Art/RedHead.png";
    //                 break;
    //             case "(2,2)":
    //                 src = "Art/RedTail.png";
    //                 break;
    //             case "(2,3)":
    //                 src = "Art/RedTile.png";
    //                 break;
    //             case "(2,4)":
    //                 src = "Art/RedKey.png";
    //                 break;
    //             case "(3,1)": // same as above but black
    //                 src = "Art/BlackHead.png";
    //                 break;
    //             case "(3,2)":   
    //                 src = "Art/BlackTail.png";
    //                 break;
    //             case "(3,3)":
    //                 src = "Art/BlackTile.png";
    //                 break;
    //             case "(3,4)":
    //                 src = "Art/BlackKey.png";
    //                 break;
    //             case "(4,1)": // same as above but white
    //                 src = "Art/WhiteHead.png";
    //                 break;
    //             case "(4,2)":
    //                 src = "Art/WhiteTail.png";
    //                 break;
    //             case "(4,3)":
    //                 src = "Art/WhiteTile.png";
    //                 break;
    //             case "(4,4)":
    //                 src = "Art/WhiteKey.png";
    //                 break;
    //             default:
    //         }
    //         change = change.substring(1, change.length-1).split(",");
    //         change[0] = parseInt(change[0]);
    //         change[1] = parseInt(change[1]);
    //         drawTile(src, change[0]*blockSize, change[1]*blockSize);
    //     }
    //     await sleep(1500-slider.value);
    // }
    
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