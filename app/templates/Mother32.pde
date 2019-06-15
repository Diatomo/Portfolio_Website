//Assets
PImage overlay;
PImage swUp;
PImage swDown;

<<<<<<< HEAD
PImage t1overlay;
PImage t1swUp;
PImage t1swDown;

PImage t2overlay;
PImage t2swUp;
PImage t2swDown;

PImage t3overlay;
PImage t3swUp;
PImage t3swDown;

=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
Scene scene;

String patchName = "Enter Patch Name Here";

void setup(){
  size(1600,1000);//dimension of canvas
  frameRate(120);
  textSize(30);
<<<<<<< HEAD
  float factor = 0.70;
=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
  //assets
  overlay = loadImage("Data/overlay.png");
  swUp = loadImage("Data/switch_up.png");
  swDown = loadImage("Data/switch_down.png");

  t1overlay = loadImage("Data/overlay.png");
  t1swUp = loadImage("Data/switch_up.png");
  t1swDown = loadImage("Data/switch_down.png");
    
  t2overlay = loadImage("Data/overlay.png");
  t2swUp = loadImage("Data/switch_up.png");
  t2swDown = loadImage("Data/switch_down.png");

  t2overlay.resize(int(t2overlay.width * factor), int(t2overlay.height * factor));
  t2swUp.resize(int(t2swUp.width * factor), int(t2swUp.height * factor));
  t2swDown.resize(int(t2swDown.width * factor), int(t2swDown.height * factor));

  t3overlay = loadImage("Data/overlay.png");
  t3swUp = loadImage("Data/switch_up.png");
  t3swDown = loadImage("Data/switch_down.png");
    
  t3overlay.resize(int(t3overlay.width * factor), int(t3overlay.height * factor));
  t3swUp.resize(int(t3swUp.width * factor), int(t3swUp.height * factor));
  t3swDown.resize(int(t3swDown.width * factor), int(t3swDown.height * factor));
    
  t3overlay.resize(int(t3overlay.width * factor), int(t3overlay.height * factor));
  t3swUp.resize(int(t3swUp.width * factor), int(t3swUp.height * factor));
  t3swDown.resize(int(t3swDown.width * factor), int(t3swDown.height * factor));
  
  //main object
  scene = new Scene();
  scene.init();
}

/*
 *
 *  class :: BoundingBox
 *
 *  Illustrated bounding boxes that collide
 *  with the mouse clicks.
 *
 */
class BoundingBox{
 
  //attributes
  float right,left,bot,top;

  /*
   *
   *  Constructor 
   *    right = right side of the box
   *    left = left side of the box
   *    bot = bottom of the box
   *    top = top of the box
   *
   */
  BoundingBox(float x, float y, float w, float h){
    right = x + w;
    left = x - w;
    bot = y + h;
    top = y - h;
  }

  /*
   *  fxn :: resize
   *    resize position values
   *    by multiplicative factor
   */
  public void resize(float x, float y, float w, float h){
    this.right = x + w;
    this.left = x - w;
    this.bot = y + h;
    this.top = y - h;
  }

  /*
   *
   *  fxn :: collision
   *    @param cursorX, cursorY :: mouse position
   *
   *  Determines whether a click made a collision
   *
   */
  public boolean collision(float cursorX, float cursorY){
    boolean collide = false; 
    if (cursorX < this.right && cursorX > this.left && 
        cursorY > this.top && cursorY < this.bot){
        collide = true;
    }
    return collide;
  }
  
  /*
   *
   *  FxN :: render
   *
   *    Renders bounding box
   *
   */
  public void render(){
    line(this.right, this.bot, this.right, this.top); //right side
    line(this.right, this.top, this.left, this.top);  //top side
    line(this.left, this.bot, this.left, this.top); // left side
    line(this.left, this.bot, this.right, this.bot); //bottom side;
  }
<<<<<<< HEAD
=======
}
/*
 *
 *  FxN :: resizeImages
 *    @param factor :: multiplicative factor
 *
 *  resizes the images (mother32, switch up, switch down);
 *
 */
void resizeImages(float factor){
    overlay.resize(int(overlay.width * factor), int(overlay.height * factor));
    swUp.resize(int(swUp.width * factor), int(swUp.height * factor));
    swDown.resize(int(swDown.width * factor), int(swDown.height * factor));
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
}

/*
 *
 *  FxN :: mouseReleased
 *
 *  Resets active object
 *  upon mouse release
 */
void mouseReleased(){
  scene.activeButton = null;
  for (Mother mother : scene.brood){
    mother.activeSwtch = null;
    mother.activeKnob = null;
    if (mother.activePatch != null){
<<<<<<< HEAD
      for (Mother mum : scene.brood){
        for (Patch patch : mum.patches){
          if (patch.bb.collision(mouseX, mouseY)){
            if (patch != mum.activePatch){
              if (patch.node == null && mother.activePatch.node == null){
                patch.hookUp(mother.activePatch);
                mother.activePatch.hookUp(patch);
              }
=======
      for (Patch patch : mother.patches){
        if (patch.bb.collision(mouseX, mouseY)){
          if (patch != mother.activePatch){
            if (patch.node == null && mother.activePatch.node == null){
              patch.hookUp(mother.activePatch);
              mother.activePatch.hookUp(patch);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
            }
          }
        }
      }
<<<<<<< HEAD
    mother.activePatch = null;
=======
      mother.activePatch = null;
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    }
  }
}

/*
 *
 *  FxN :: mouseDragged
 *
 *  While mouse is being dragged it will
 *  turn the dial on the knobs.
 *
 */
void mouseDragged(){
  for (Mother mother : scene.brood){
    if (mother.activeKnob != null){
      mother.activeKnob.turn();
    }
    if (mother.activePatch != null){
      mother.activePatch.hookingUp();
    }
  }
}

void keyPressed() {
  if (keyCode == BACKSPACE) {
    if (patchName.length() > 0) {
      patchName = patchName.substring(0, patchName.length()-1);
    }
  } 
  else if (keyCode == DELETE) {
    patchName = "";
  } 
  else if (keyCode != SHIFT && keyCode != CONTROL && keyCode != ALT) {
    patchName = patchName + key;
  }
}

//===========================================
//UTILITY 

/*
 *
 *  class :: Button
 *
 *  Buttons to add and remove mothers
 *  also to save the output.
 *
 */
class Button{

  //attributes
  float posX, posY, w, h, gap;
<<<<<<< HEAD
  boolean animate;
=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
  BoundingBox bb;
  String label;

  /*
   *
   *  Constructor
   *    x = posiion X coord
   *    y = position y coord
   *    w = width of rectangle
   *    h = height of rectangle
   *    gap = distance from text to button.
   *    label = label for button
   *
   */
  Button(float x, float y, String label){
    this.w = 20;
    this.h = 20;
    this.gap = 100;
    this.posX = x;
    this.posY = y;
    this.label = label;
<<<<<<< HEAD
    this.animate = false;
=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    this.bb = new BoundingBox(x,y,w,h);
  }

  /*
   *  fxn :: resize
   *    resize position values
   *    by multiplicative factor
   */
  public void resize(float factor){
    this.posX = this.posX * factor;
    this.posY = this.posY * factor;
    this.w = this.w * factor;
    this.h = this.h * factor;
  }

  public void reposBB(){
    this.bb = new BoundingBox(this.posX,this.posY,this.w,this.h);
  }

<<<<<<< HEAD

  private void animation(){ 
    float rate = 0.5;
    float maxDim = 20;
    float minDim = 5;
    if (animate){
      if (this.w > minDim && this.h > minDim){
        this.w = this.w - rate;
        this.h = this.h - rate;
      }
      else{
        animate = false;
      }
    }
    else{
      if (this.w < maxDim && this.h < maxDim){
        this.w = this.w + rate;
        this.h = this.h + rate;
      }
    }
  }

=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
  /*
   *
   *  FxN :: render
   *
   *    Renders rectangle and label
   *
   */
  public void render(){
    fill(0);
    rectMode(CENTER);
    rect(this.posX, this.posY, this.w, this.h);
    rectMode(CORNER);
<<<<<<< HEAD
    animation();
    if (this.label == "add"){
      text(this.label, this.posX - this.gap + 22, this.posY + 10);

    }
    else if (this.label == "remove"){
      text(this.label, this.posX - this.gap - 30, this.posY + 10);

    }
    else if (this.label == "save"){
      text(this.label, this.posX - this.gap + 12, this.posY + 10);
    }
=======
    text(this.label, this.posX - this.gap, this.posY);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
  }

}

/*
 *
 *  class :: Scene
 *
 *  Controls all elements in the scene.
 *
 */
class Scene{
  
  //attributes
  ArrayList<Mother> brood; //container for mothes
  float[] buttX = {1550,1550,1550};
  float[] buttY = {40, 100,160};
  private int numButtons = 3;
  StringList labels = new StringList();
  private Button[] buttons = new Button[numButtons];
  Mother mother1, mother2, mother3; //mother synthesizer
  Button activeButton;



  /*
   *
   *  Constructor
   *
   */
  Scene(){
    this.brood = new ArrayList<Mother>();
<<<<<<< HEAD
    this.mother1 = new Mother(125, 150);
=======
    this.mother1 = new Mother(100, 100);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    this.mother2 = new Mother(0, 0);
    this.mother3 = new Mother(0, 0);
    this.mother1.init();
    this.mother2.init();
    this.mother3.init();
    this.brood.add(this.mother1);
    this.labels.append("add");
    this.labels.append("remove");
    this.labels.append("save");
    this.activeButton = null;
  }

  public void init(){
    //init buttons
    for (int i = 0; i < numButtons; i++){
      buttons[i] = new Button(this.buttX[i], this.buttY[i], this.labels.get(i));
    }
  }

  /*
   *  fxn :: add
   *
   *    add a mother from the container
   *    then scales
   *
   */
<<<<<<< HEAD
  public void removeRepos(){
      if (this.brood.size() == 1){
        this.mother1.posX = 125;
        this.mother1.posY = 150;
      }
      else if (this.brood.size() == 2){
        float posX = 250;
        this.mother1.posX = posX;
        this.mother1.posY = 25;
        this.mother2.posX = posX;
        this.mother2.posY = 350;
      }
      else if (this.brood.size() == 3){
        float posX = 700;
        this.mother1.posX = posX;
        this.mother1.posY = 50;
        this.mother2.posX = posX;
        this.mother2.posY = 500;
        this.mother3.posX = posX;
        this.mother3.posY = 950;
      }
  }

  public void addRepos(){
      if (this.brood.size() == 1){
        this.mother1.posX = 125;
        this.mother1.posY = 150;
      }
      else if (this.brood.size() == 2){
        float posX = 500;
        this.mother1.posX = posX;
        this.mother1.posY = 50;
        this.mother2.posX = posX;
        this.mother2.posY = 700;
      }
      else if (this.brood.size() == 3){
=======
  public void add(){
    float factor = 0.70;
    if (this.brood.size() < 3){    
      if (this.brood.size() == 1){
        this.brood.add(this.mother2);
        this.mother1.posX = 400;
        this.mother1.posY = 50;
        this.mother2.posX = 400;
        this.mother2.posY = 700;
        this.mother3.resize(factor);
      }
      else if (this.brood.size() == 2){
        this.brood.add(this.mother3);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
        float posX = 700;
        this.mother1.posX = posX;
        this.mother1.posY = 50;
        this.mother2.posX = posX;
        this.mother2.posY = 500;
        this.mother3.posX = posX;
        this.mother3.posY = 950;
      }
<<<<<<< HEAD
  }


  private void unhookPatches(){
    for (Mother mother : brood){
      for (Patch patch : mother.patches){
        patch.breakUp();
      }
=======
      this.scale(factor);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    }
  }

  /*
   *  fxn :: remove
   *
   *    removes a mother from the container
   *    then scales
   *
   */
  private void remove(){
<<<<<<< HEAD
    float factor = 10.0/7.0;
    if (this.brood.size() > 1){
      if (this.brood.size() == 3){
        this.brood.remove(this.mother3);
        this.mother3.resize(factor);
      }
      else if (this.brood.size() == 2){
        this.brood.remove(this.mother2);
        this.mother2.resize(factor);
        this.mother3.resize(factor);
      }
    this.removeRepos();
    this.scale(factor);
    }
  this.unhookPatches();
  }

  private void add(){
    float factor = 0.70;
    if (this.brood.size() < 3){    
      if (this.brood.size() == 1){
        this.brood.add(this.mother2);
        this.mother3.resize(factor);
      }
      else if (this.brood.size() == 2){
        this.brood.add(this.mother3);
      }
    this.addRepos();
    this.scale(factor);
  }
  this.unhookPatches();
=======
    float factor = 1.25;
    if (this.brood.size() > 1){
      if (this.brood.size() == 3){
        this.brood.remove(this.mother3);
      }
      else if (this.brood.size() == 2){
        this.brood.remove(this.mother2);
      }
    this.scale(factor);
    }
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
  }

  private void saveImage(){
    for (Mother mother : brood){
      mother.update();
    }
    String fmt = ".jpg";
    save(patchName + fmt);
    //saveFrame(patchName + fmt);
  }

  /*
   *  fxn :: scale
   *    scale position values
   *    by multiplicative factor
   */
  private void scale(float factor){
<<<<<<< HEAD
=======
    resizeImages(factor);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    for (Mother mother : brood){
      mother.resize(factor);
    }
    for (Mother mother : brood){
      mother.reposition(); 
    }
  }

  private void updateButton(){
    for (Button button : buttons){
      button.render();
      button.bb.render();
      if (mousePressed){
        if (button.bb.collision(mouseX, mouseY)){
          if (this.activeButton == null){
            this.activeButton = button;
<<<<<<< HEAD
            this.activeButton.animate = true;
=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
            if (this.activeButton.label == "add"){
              this.add();
            }
            else if (this.activeButton.label == "remove"){
              this.remove();
            }
            else if (this.activeButton.label == "save"){
              this.saveImage(); 
            }
          }
        }
      }
    }
  }

  public void update(){
    this.updateButton();
    for (Mother mother : brood){
      mother.update();
    }
  }

  public void render(){
    for (Button button : buttons){
      button.render();
    }
    for (Mother mother : brood){
      mother.render();
    }
  }
}

//===========================================
/*
 *
 *  class :: Switches
 *
 *  container class for the switch images
 *  and asset animations
 */
class Switch{

  //attributes
  PImage img;
  boolean state;
  float posX, posY, w, h;
  float alarmTime;
  boolean animation, isSet;
  BoundingBox bb;
  
  //constructor
  Switch(float x,float y){
    //defaults
    w = 25;//bounding box width
    h = 25;//bounding box height
    state = false;//sprite toggle {up || down}
    
    bb = new BoundingBox(x,y,w,h);
    //attributes
    img = swDown;
    posX = x;
    posY = y;
  }

  /*
   *  fxn :: switchState
   *    When left click it changes the state
   *    and renders a different image
   */
  private void switchState(){
      state = !state;
      if (state){
        img = swUp;
      }
      else{
        img = swDown;
      }
    }

  /*
   *  fxn :: resize
   *    resize position values
   *    by multiplicative factor
   */
  public void resize(float factor){
    this.posX = this.posX * factor;
    this.posY = this.posY * factor;
    this.w = this.w * factor;
    this.h = this.h * factor;
    this.bb = new BoundingBox(this.posX, this.posY, this.w, this.h);
  }

  public void reposBB(){
    this.bb = new BoundingBox(this.posX,this.posY,this.w,this.h);
  }
  /*
   *  fxn :: render
   *    renders the image
   *    assigned by the state
   */
  public void render(){
    if (state){
      if (scene.brood.size() == 1){
        img = t1swUp;
      }
      else if (scene.brood.size() == 2){
        img = t2swUp;
      }
      else if (scene.brood.size() == 3){
        img = t3swUp;
      }
    }
    else{
      if (scene.brood.size() == 1){
        img = t1swDown;
      }
      else if (scene.brood.size() == 2){
        img = t2swDown;
      }
      else if (scene.brood.size() == 3){
        img = t3swDown;
      }
    }
    image(img, this.posX, this.posY);
  }
}
//===========================================

//===========================================
/*
 *
 *  class : Knobs 
 *
 *  Container class for the knobs
 *  renders a line that can spin around
 *  the center.
 */
class Knob{

  float posX, posY, w, h; //positions
  float radius; //radius
  float angle;  //degree of rotation
  float currMouse, prevMouse; //controller values
  boolean active;
  BoundingBox bb;
  Knob(float x, float y){
    w = 50; //bounding box width
    h = 50; //bounding box height
    angle = 270; //default angle degrees {0,360}
    radius = 28; //radius length :: hardcoded
    bb = new BoundingBox(x,y,w,h);
    posX = x;
    posY = y;
  }

  /*
   *  fxn :: setMousePos
   *
   *  initializes the currMouse value
   *
   */
  public void setMousePos(){
    this.currMouse = mouseY;
  }
  
  /*
   *  fxn :: turn
   *
   *  when the mouse is dragged
   *  it calls the function to 
   *  increment or decrement
   *  an angle value
   *
   */
  public void turn(){
    float incr = 5;
    this.setMousePos();
    if (currMouse - prevMouse > 0){
      angle += incr % 360;
      prevMouse = currMouse;
    }
    else if (currMouse - prevMouse < 0){
      angle -= incr % 360;
      prevMouse = currMouse;

    }
  }

  /*
   *  fxn :: resize
   *    resize position values
   *    by multiplicative factor
   */
  public void resize(float factor){
    this.posX = this.posX * factor;
    this.posY = this.posY * factor;
    this.w = this.w * factor;
    this.h = this.h * factor;
    this.radius = this.radius * factor;
    this.bb.resize(this.posX, this.posY, this.w, this.h);
  }

  public void reposBB(){
    this.bb = new BoundingBox(this.posX,this.posY,this.w,this.h);
  }
  /*
   *  fxn :: render
   *
   *  renders the line
   *    
   */
  public void render(){
    float posXrot = this.posX + cos(radians(this.angle)) * this.radius;
    float posYrot = this.posY + sin(radians(this.angle)) * this.radius;
    line(this.posX, this.posY, posXrot, posYrot);
  }
}
//===========================================



//===========================================
/*
 *
 *  class : Patch
 *
 *  
 *
 */
class Patch{
 
  //attributes
  float posX, posY, w, h;
  float radius;
  BoundingBox bb;
  boolean snapped;
  boolean snapping;
  color c;
  Patch node;

  /*
   *
   *  Constructor
   *
   */
  Patch(float x, float y){
    w = 17;
    h = 17;
    bb = new BoundingBox(x,y,w,h);
    snapped = false;
    posX = x;
    posY = y;
    radius = 5;
    c = color(random(255), random(255), random(255));
  }



  /*
   *  fxn :: hookingUp
   *
   *    temp render while mouse is held down.
   *
   */
  public void hookingUp(){
    line(this.posX, this.posY, mouseX, mouseY);
  }

  /*
   *  fxn :: hookUp
   *
   *    consumate relationship with
   *    another node
   *
   */
  public void hookUp(Patch node){
    this.node = node;
  }

  /*
   *  fxn :: breakUp
   *
   *    break relationship with another node
   *
   */
  public void breakUp(){
    node = null;
  }

  /*
   *  fxn :: resize
   *    resize position values
   *    by multiplicative factor
   */
  public void resize(float factor){
    this.posX = this.posX * factor;
    this.posY = this.posY * factor;
    this.w = this.w * factor;
    this.h = this.h * factor;
    this.radius = this.radius * factor;
    this.bb.resize(this.posX, this.posY, this.w, this.h);
  }

  public void reposBB(){
    this.bb = new BoundingBox(this.posX,this.posY,this.w,this.h);
  }
  /*
   *  fxn :: render
   *
   *  renders the vertex 
   *  or snapping point
   *    
   */
  public void render(){
    fill(255);
    //ellipse(this.posX, this.posY, this.radius, this.radius);
    if(this.node != null){
      strokeWeight(5);
<<<<<<< HEAD
      stroke(125, 75);
      line(this.posX, this.posY, this.node.posX, this.node.posY);
      stroke(0,255);
=======
      line(this.posX, this.posY, this.node.posX, this.node.posY);
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
      strokeWeight(2);
    }
  }
}
//===========================================



//===========================================
class Mother{

  //attributes
  private int numSwitches = 9;
  private int numKnobs = 14;
  private int numPatchesX = 4;
  private int numPatchesY = 8;
  float[] switchX = {242,879,242,487,606,727,970,485,720};
  float[] switchY = {87,87,208,208,208,208,208,329,329};
  float[] knobX = {120,363,483,629,775,970,120,363,848,199,364,606,849,970};
  float[] knobY = {85,85,85,85,85,85,205,205,205,327,328,327,325,326};
  float sPatchX = 1082;
  float sPatchY = 77;
  float patchSpace = 57;
  private Switch[] switches = new Switch[numSwitches];
  private Knob[] knobs = new Knob[numKnobs];
  private Patch[] patches = new Patch[numPatchesX * numPatchesY];
  private PImage synth;
  private float posX, posY;
  Switch activeSwtch;
  Knob activeKnob;
  Patch activePatch;

  /*
   *
   *  Constructor
   *
   *
   */
  Mother(float x, float y){
    activeSwtch = null;
    activeKnob = null;
    posX = x;
    posY = y;
    synth = overlay;
  }

  /*
   *
   *  FxN :: init
   *    
   *    Creates components and sets the components
   *    on the canvas.
   *
   */
  void init(){
    
    //init switches
    for (int i = 0; i < numSwitches; i++){
      this.switches[i] = new Switch(switchX[i] + this.posX, switchY[i] + this.posY); 
    }

    //init knobs
    for (int i = 0; i < numKnobs; i++){
      this.knobs[i] = new Knob(knobX[i] + this.posX, knobY[i] + this.posY);
    }

    //init patches
    float tempX = this.sPatchX;
    float tempY = this.sPatchY;
    for (int i = 0; i < numPatchesY; i++){
      for (int j = 0; j < numPatchesX; j++){
        patches[i * numPatchesX + j] = new Patch(tempX + this.posX, tempY + this.posY);
        tempX += patchSpace;
      }
      tempX = sPatchX;
      tempY += patchSpace;
    }
  }

  /*
   *
   *  FxN :: resize
   *    @param factor :: multiplicative factor to scale by
   *    
   *  resizes sizes through by a factor
   *
   */
  void resize(float factor){

    //resize switches
    for (int i = 0; i < numSwitches; i++){
      switchX[i] = switchX[i] * factor;
      switchY[i] = switchY[i] * factor;
      switches[i].resize(factor);
    }
    
    //resize knobs
    for (int i = 0; i < numKnobs; i++){
      knobX[i] = knobX[i] * factor;
      knobY[i] = knobY[i] * factor;
      knobs[i].resize(factor);
    }

    //resize patches
    sPatchX = sPatchX * factor;
    sPatchY = sPatchY * factor;
    patchSpace = patchSpace * factor;
    for (int i = 0; i < numPatchesX * numPatchesY; i++){
      patches[i].resize(factor);
    }
    this.posX = this.posX * factor;
    this.posY = this.posY * factor;
  }


  /*
   *
   *  FxN :: reposition
   *    
   *  reposition components on the canvas
   *
   */
  void reposition(){

    //reposition switches
    for (int i = 0; i < numSwitches; i++){
      this.switches[i].posX = switchX[i] + this.posX; 
      this.switches[i].posY = switchY[i] + this.posY;
      this.switches[i].reposBB();
    }

    //reposition knobs
    for (int i = 0; i < numKnobs; i++){
      this.knobs[i].posX = knobX[i] + this.posX;
      this.knobs[i].posY = knobY[i] + this.posY;
      this.knobs[i].reposBB();
    }

    //reposition patches
    float tempX = this.sPatchX;
    float tempY = this.sPatchY;
    for (int i = 0; i < numPatchesY; i++){
      for (int j = 0; j < numPatchesX; j++){
        patches[i * numPatchesX + j].posX = tempX + this.posX;
        patches[i * numPatchesX + j].posY = tempY + this.posY;
        patches[i * numPatchesX + j].reposBB();
        tempX += patchSpace;
      }
      tempX = sPatchX;
      tempY += patchSpace;
    }


  }

  /*
   *
   *  FxN :: updateSwitch
   *    
   *    collision handler
   *    render handler
   *
   */
  private void updateSwitch(){
    imageMode(CENTER);
    for (Switch swtch : switches){
      swtch.render();
      swtch.bb.render();
      if (mousePressed){ //collision handler
        if(swtch.bb.collision(mouseX, mouseY)){
          if (this.activeSwtch == null){
            this.activeSwtch = swtch;
            swtch.switchState();
          }
        }
      }
    }
  imageMode(CORNER);
  }

  /*
   *
   *  FxN :: updateKnob
   *    
   *    collision handler
   *    render handler
   *
   */
  private void updateKnob(){
    for (Knob knob : knobs){
      knob.render();
      knob.bb.render();
      if (mousePressed){ //collision handler
        if(knob.bb.collision(mouseX, mouseY)){
          if (this.activeKnob == null){
            this.activeKnob = knob;
          }
        }
      }
    }
  }

  /*
   *
   *  FxN :: updatePatch
   *    
   *    collision handler
   *    render handler
   *
   */
  private void updatePatch(){
    for (Patch patch : patches){
      patch.render();
      patch.bb.render();
      if (patch == this.activePatch){
        patch.hookingUp();
      }
      if (mousePressed){  //collision handler
        if(patch.bb.collision(mouseX, mouseY)){
<<<<<<< HEAD
          boolean otherActive = false;
          for (Mother mum : scene.brood){
            if (mum.activePatch != null){
              otherActive = true;
            }
          }
          if (otherActive == false){
            if(this.activePatch == null){
              this.activePatch = patch;
              if (this.activePatch.node != null){
                this.activePatch.node.breakUp();
                this.activePatch.breakUp();
              }
=======
          if(this.activePatch == null){
            this.activePatch = patch;
            if (this.activePatch.node != null){
              this.activePatch.node.breakUp();
              this.activePatch.breakUp();
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
            }
          }
        }
      }
    }
  }
  /*
   *
   *  FxN :: update
   *    
   *    updates components
   *    
   *
   */
  public void update(){
    updateSwitch();
    updateKnob();
    updatePatch();
  }

  /*
   *  FxN :: render
   *  
   *    Renders image
   *
   */
  public void render(){
<<<<<<< HEAD
    if (scene.brood.size() == 1){
      overlay = t1overlay;
    }
    else if (scene.brood.size() == 2){
      overlay = t2overlay;
    }
    else if (scene.brood.size() == 3){
      overlay = t3overlay;
    }
=======
>>>>>>> b2dcd4164f09167135930b975e5dea0f7fd11e25
    image(overlay,this.posX,this.posY);
  }
}
//===========================================


/*
 *
 *  fxn :: draw
 *
 *    
 *
 */
void draw(){
  background(255,255,255);
  strokeWeight(2);
  fill(0);
  text("Patch Name:",0,0,width,height);
  text(patchName,185,0, width, height);
  scene.render();
  scene.update();
}




