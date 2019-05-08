Bird bird;
ArrayList<Pipe> pipes = new ArrayList<Pipe>();
int score = 0;

public void setup(){
  size(800, 600);
  bird = new Bird();
  pipes.add(new Pipe());
}

public void draw(){
  background(0); //<>//
  bird.update();
  bird.show(); //<>//
  
  

  if(frameCount % 250 == 0){
      pipes.add(new Pipe());
  }
  
  for(int i = 0; i < pipes.size(); i++){
    pipes.get(i).show();
    
    // Create temp variables for each pipe set to check vs bird position
    int tempLeft = pipes.get(i).x;
    int tempRight = tempLeft + pipes.get(i).rect_width;
    float tempTopLip = pipes.get(i).top_lip;
    float tempBottomLip = pipes.get(i).bottom_lip;
    
    // Check if the bird is in a pipe
    if(bird.x > tempLeft && bird.x < tempRight){
      if(bird.y < tempTopLip || bird.y > tempBottomLip){
        // If it is, kill the bird
        bird.killBird();
      }
    }
    pipes.get(i).update();
  }
  
  // Add points for time lived
  if(frameCount % 25 == 0){
    score++;
  }
  
  // Display score or dead
  if(!bird.checkHealth()){
    textSize(20);
    text("Score: " + str(score), 10, 20);
  }
  else{
    textSize(20);
    text("Player Dead!", 10, 20);
  }
} //<>//

public void keyPressed(){
  // Flap if alive when enter is pressed
  if(!bird.checkHealth()){
    if(key == ENTER){
      bird.flap();
    }
  }
}
