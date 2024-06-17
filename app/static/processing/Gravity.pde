
/*
  Author : Charles Stevenson -Diatom-
  DATE :   1/18/2016
  Purpose:
    This program is my first attempt at processing. I decided I wanted to make a gravity simulator.
    Spawn in planets with a mouse click and watch them orbit around a central point. There could 
    be a lot more done with this. A Game, Better Visuals, 3D?
    
  Program Structure:
      There is a class that stores numbers tied to objects, like pos,vel,and acc, and mass.
      When mouse is pressed an object is created and so is an image, that is accessible
      in the group PShape and also the class itself. To modify and animate the image I used
      the PShape functions as I wasn't able to modify values tradiationally, that is, plug in
      a variable to an ellipse()fxn and increment that parameter. Therefore it felt a little strange
      to me. However, next time I would want to just manipulate the gravity and distance within the class
      and also make the sun a more dynamic peice.
*/

//initials
ArrayList<Planet> planets = new ArrayList<Planet>(); //Array of class objects
ArrayList<Planet> suns = new ArrayList<Planet>();
ArrayList<Planet> blackHoles = new ArrayList<Planet>();
ArrayList<ArrayList<Planet>> celBodies = new ArrayList<ArrayList<Planet>>();
int timer = 0;
int zoomCounter = 0;
float[] rgb = new float[3];
float GRAVITY = 4;
boolean[] reverse = new boolean[3];

//SETUP
void setup () {
 //init windows data
 size(2000,1000);  
 colorMode(HSB,100);
 frameRate(120);
 //init groups
 celBodies.add(planets);
 celBodies.add(suns);
 celBodies.add(blackHoles);
 Planet sun = createPlanet(width/2, height/2, 600.0,55,0,0,0,0);
 sun.addPlanet();
 suns.add(sun);
 
 timer = millis();//start timer
 for (int i = 0; i<3;i++){//initialize HSB values
    rgb[i] = int(random(10,90));
 }
 for (int i = 0; i < reverse.length; i++){//initialize reverse boolean array
  reverse[i] = false;
}
}
//=================================================
//HELPER FUNCTIONS
//=================================================
//change color of background
float[] changecolor(){
    for (int i = 0;i<rgb.length;i++){
      if (rgb[i] >= 90){
        reverse[i] = true;
      }
      else if (rgb[i] <= 10){
        reverse[i] = false;
      }
      if (reverse[i]){
        rgb[i] -= 0.2;
      }
      else{
        rgb[i] += 0.2;
      }
    }
  return rgb;
}
//distance
float distance(Planet sun , Planet planet){ 
   return sqrt(sq((sun.posX - planet.posX)) + sq((sun.posY - planet.posY)));
}
float distanceXY(Planet sun, float x, float y){
 return sqrt(sq((sun.posX - x)) + sq((sun.posY - y))); 
}

Planet closestSun(float x, float y){
   Planet sun = suns.get(0);
   float dist = 0;
   float tempDist = 0;
   for (Planet Sun : suns){
     tempDist = distanceXY(Sun, x, y);
     if (dist < tempDist){
       dist = tempDist;
       sun = Sun;
     }
   }
   return sun;
}

//gravitational formula -newton-
//F = ma ; a = (G(m1xm2)/r^2)/m2
float gravity(Planet sun, Planet planet){
   float num = (sun.mass*planet.mass); //(product of masses)
   float den = sq(distance(sun,planet)); //(inverse square)
   return GRAVITY*(num/den)/planet.mass;
}

//==============================================
//INPUTS
//==============================================
//ADD OR REMOVE SUN OR PLANET
void mousePressed() {
  Planet pointer = null;
  boolean removed = false;
  if (mouseButton == LEFT){
      for (Planet planet: planets){
        if ((mouseX < (planet.posX + planet.mass)) && (mouseY < (planet.posY + planet.mass)) &&
            (mouseY > (planet.posY - planet.mass)) && (mouseX > planet.posX - planet.mass)){
              pointer = planet;
        }
      }
  if (pointer != null){
    planets.remove(pointer);
    removed = true;
  }
    if(!removed){
      Planet earth = createPlanet(0,0, 0, int(random(0,40)), 1, 1,1,1); //create a planet object
      earth.addPlanet(); //create a shape
      planets.add(earth); //add Earth to the Array List
    }
  }
}

//ZOOM
void mouseWheel(MouseEvent event){
 float e = event.getCount();
   if (e > 0){
    //zoomOut(); 
   }
   else if (e < 0){
     //zoomIn();
   }
}
/*void zoomIn(){
  if (zoomCounter != 50){
    zoomCounter++;
    for (ArrayList<Planet> arrays : celBodies){
      for (Planet planet : arrays){
        planet.circle.scale(1.05);
      }
    }
  }
}*/
/*void zoomOut(){
  if (zoomCounter != -50){
    zoomCounter--;
    for (ArrayList<Planet> arrays : celBodies){
      for (Planet planet : arrays){
        planet.circle.scale(0.95);
      }
    }
  }
}*/
//ADD BLACKHOLE
void keyPressed(){
  Planet pointer = null;
  boolean removed = false;
  if(key == ENTER){
   for (Planet blackHole: blackHoles){
      if ((mouseX > (blackHole.posX - blackHole.mass/10)) && (mouseY > (blackHole.posY - blackHole.mass/10)) &&
          (mouseY < (blackHole.posY + blackHole.mass/10)) && (mouseX < (blackHole.posX + blackHole.mass/10))){
            pointer = blackHole;
      }
    }
    if (pointer != null){
      blackHoles.remove(pointer);
      removed = true;
    }
    if (!removed){
 Planet blackHole = createPlanet(0,0 ,3000,100,0,0,0,0);
      
      blackHole.addPlanet();
      blackHoles.add(blackHole);
    }
  }
}
//======================================
//CLASS
//======================================
class Planet{
  //constructor
  float velX,velY, posX, posY, accX, accY, radius, mass;
  boolean stuck;
  Planet(float m, int r, float x, float y, float vX, float vY, float aX, float aY){
     mass = m; //mass
     radius = r;//radius
     posX = x; //positionX
     posY = y; //positionY
     accX = aX;//accelerationX
     accY = aY;//accelerationY
     velX = vX;//velocityX
     velY = vY;//velocityY
     stuck = false;
  }
  void addPlanet(){
    shapeMode(CENTER);
    ellipse(this.posX, this.posY, this.radius, this.radius);
  }
//UPDATES
  void planetUpdate(){
    int constant = 20;
    ellipse(this.posX,this.posY,this.radius,this.radius);  //draw 
    //FORCING ARE POINTING IN WRONG DIRECTIONS;
    for (Planet sun : suns){
      if ((this.posX < sun.posX - constant || this.posY < sun.posY - constant) ||
          (this.posY > sun.posY + constant || this.posX > sun.posX + constant)){
          this.accX = (gravity(sun, this)) * (sun.posX - this.posX)/distance(sun, this); //vector multiplied to the acceleration / distance to keep number small
          this.accY = (gravity(sun, this)) * (sun.posY - this.posY)/distance(sun,this); //vector multiplied to the acceleration / distance to keep number small
          this.velX += this.accX; //add acc to vel
          this.velY += this.accY; //add acc to vel
          //circle.translate(this.velX, this.velY); //animate circle to updated coordinates
          //print("velX = " + velX + "\n");
          //print("velY = " + velY + "\n");
          this.posX += this.velX; //update those coordinates
          this.posY += this.velY; //update those coordinates
      }
      else{
        this.stuck = true;
      }
    }
  }

  void sundate(){
     ellipse(this.posX,this.posY,this.radius,this.radius);  //draw
     for (Planet blackHole : blackHoles){
          this.accX = (gravity(blackHole, this)) * (blackHole.posX - this.posX)/distance(blackHole,this); //vector multiplied to the acceleration / distance to keep number small
          this.accY = (gravity(blackHole, this)) * (blackHole.posY - this.posY)/distance(blackHole,this); //vector multiplied to the acceleration / distance to keep number small
          print("accx = \n" + accX);
          print("accy = \n" + accY);
          this.velX += this.accX; //add acc to vel
          this.velY += this.accY; //add acc to vel
          //circle.translate(this.velX, this.velY); //animate circle to updated coordinates
          this.posX += this.velX; //update those coordinates
          this.posY += this.velY; //update those coordinates
     }
  }
     void blackHoleUpdate(){
       //shape(this.circle); 
     }
}

//CREATE ATTRIBUTES FOR CLASS
Planet createPlanet(float posX, float posY, float mass, int radius, float vX, float vY, float accX, float accY){
  float x = 0;
  float y = 0;
  if (mass == 0){
    mass = int(random(5,50));
    radius = (int) mass;
  }
  if (posX == 0 && posY == 0){
  x = mouseX;
  y = mouseY;
  }
  else{
    x = posX;
    y = posY;
  }
  if(vX == 1 && vY == 1){
    Planet Sun = closestSun(x,y);
    vX = random(-2,2);//sqrt((GRAVITY*(Sun.mass))/distanceXY(Sun, x, y));
    vY = random(-2,2);//sqrt(((GRAVITY*(Sun.mass)))/distanceXY(Sun, x, y));
  }
  //if(accX == 1 && accY == 1){
    //Planet Sun = closestSun(x,y);
    accX = 0; //GRAVITY * (Sun.mass + mass) / distanceXY(Sun, x, y);
    accY = 0;//GRAVITY * (Sun.mass + mass) / distanceXY(Sun, x, y);
  //}
  return new Planet(mass,radius,x,y,vX,vY,accX,accY);
}

//DRAW
void draw(){
  if (timer%2 == 0){
    rgb = changecolor();
  }
  background(0,0,0); //refresh the screen with background
  for (Planet planet : planets){ //cycle through each planet spawned and update and draw them
    planet.planetUpdate();//update movement 
  }
  for (int i = planets.size() - 1; i >= 0; i--){
   Planet planet = planets.get(i);
   if (planet.stuck == true){
     planets.remove(i);
   }
  }
  for (Planet sun : suns){
    sun.planetUpdate();
 }
 for (Planet blackHole : blackHoles){
     blackHole.blackHoleUpdate();
 }
  timer++;
}
