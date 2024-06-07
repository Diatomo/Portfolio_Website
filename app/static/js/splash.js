

var debug = false;

//===============================
//          SETUP
//===============================
// Create the PixiJS application
const app = new PIXI.Application({
    resizeTo: window,
    backgroundColor: 0xffffff, // Background color
});

// Append the canvas to the HTML container
document.getElementById('pixi-container').appendChild(app.view);
document.body.appendChild(app.view);

//===============================
//          UTILITY
//===============================

/*
 *  getRandomColor
 *
 *  returns random color
 */
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

// Generate a random number between -4 and -1 or between 1 and 4
function getRandomVel() {
    const randomNumber = Math.random(); // Generate a random number between 0 and 1

    if (randomNumber < 0.5) {
        // Generate a random number between -4 and -1
        return Math.floor(Math.random() * 4) - 4;
    } else {
        // Generate a random number between 1 and 4
        return Math.floor(Math.random() * 4) + 1;
    }
}

function getRandomRadius() {
    const MAXRADIUS = 50;
    const MINRADIUS = 20;
    return Math.floor(MINRADIUS + Math.random() * MAXRADIUS);

}

function printValues(idx) {
    console.log('positionX: ' + diatoms[idx]['attr']['posX']);
    console.log('positionY: ' + diatoms[idx]['attr']['posY']);
}

//===============================
//          DIATOMS
//===============================

/*
 *  0xff76ce - pink
 *  0xfdffc2 - yellow
 *  0x94ffd8 - green
 *  0xa3d8ff - blue
 *
 */
const colors = [0xff76ce, 0xfdffc2, 0x94ffd8, 0xa3d8ff];

var diatoms = {}
var diatomAttr = {}
var id = 0;

function createDiatom(){

    const d = new PIXI.Graphics();
    var r = getRandomRadius();
    var x = getRandomInt(window.innerWidth);
    var y = getRandomInt(window.innerHeight);
    d.lineStyle(2, colors[getRandomInt(colors.length)]);  //(thickness, color)
    d.beginFill(colors[getRandomInt(colors.length)]);
    d.drawCircle(0, 0, r);
    d.endFill();

    var attr = {}
    attr['posX'] = x;
    attr['posY'] = y;
    attr['velX'] = getRandomVel();
    attr['velY'] = getRandomVel();
    attr['radius'] = r;

    var diatom = {'pixiObj': d, 'attr': attr};
    diatoms[id] = diatom;
    console.log(d);
    app.stage.addChild(diatoms[id]['pixiObj'])
    id++;
}

const NUM_OF_DIATOMS = 50;
for (let i = 0; i < NUM_OF_DIATOMS; i++){
    createDiatom();
}

//===============================
//          TITLE
//===============================

const style = new PIXI.TextStyle({
    fontFamily: "\"Lucida Console\", Monaco, monospace",
    fontSize: 60,
    fontVariant: "small-caps",
    fontWeight: "bold",
    fill: 0xFF8F4A,
    align: 'center'
});


// Create a new text element
const text = new PIXI.Text('Diatom Projects', style);

// Set the position of the text element
text.x = app.view.width / 2;
text.y = app.view.height / 3;
text.anchor.set(0.5); // Center the text element

// Add the text element to the stage
app.stage.addChild(text);



//===============================
//          BUTTON
//===============================
// Function to create a button
function createButton(x, y, width, height, text) {
    const button = new PIXI.Container();
    //const graphics = new PIXI.Graphics();

    // Draw the button background
    //graphics.beginFill(0xffffff);
    //graphics.drawRect(0, 0, width, height);
    //graphics.endFill();

    // Create the button text
    const buttonText = new PIXI.Text(text, { fontFamily: "\"Lucida Console\", Monaco, monospace", fontSize: 24, fill: 0x0000FF });
    buttonText.x = width / 2 - buttonText.width / 2;
    buttonText.y = height / 2 - buttonText.height / 2;

    // Add the graphics and text to the button container
    //button.addChild(graphics);
    button.addChild(buttonText);

    // Position the button
    button.x = x;
    button.y = y;

    // Make the button interactive
    button.interactive = true;
    button.buttonMode = true;

    // Set up the click event
    button.on('pointerdown', () => {
        window.location.href = '/index';
    });

    // Set up the hover events to change text color
    button.on('pointerover', () => {
        buttonText.style.fill = 0x7DF9FF; // Hover text color
    });

    button.on('pointerout', () => {
        buttonText.style.fill = 0x0000ff; // Default text color
    });

    return button;
}

let width = 100;
let height = 50;
const button = createButton(window.innerWidth/2 - width/2, window.innerHeight/2 - 2*height, width, height, 'Enter');
app.stage.addChild(button);

//===============================
//          GAMELOOP
//===============================

function updatePosition(key) {
    var dPixi = diatoms[key]['pixiObj'];
    var dAttr = diatoms[key]['attr'];
    const radius = dAttr['radius'];
    var padding = 10;
    var canvasWidth = window.innerWidth + 2*radius + padding;
    var canvasHeight = window.innerHeight + 2*radius + padding;
    dAttr['posX'] = ((((dAttr['posX'] + dAttr['velX']) % canvasWidth)) + canvasWidth) % canvasWidth;
    dAttr['posY'] = ((((dAttr['posY'] + dAttr['velY']) % canvasHeight)) + canvasHeight) % canvasHeight;
    dPixi.x = dAttr['posX'];
    dPixi.y = dAttr['posY'];

    if (debug) {
        printValues(0);
    }
}

function gameLoop() {

    Object.keys(diatoms).forEach(key => {
        updatePosition(key);
    })
}

// Add the update function to the application's ticker
app.ticker.add(gameLoop);
