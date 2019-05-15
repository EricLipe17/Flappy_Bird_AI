Bird bird;

ArrayList<Pipe> pipes = new ArrayList<Pipe>();

int score = 0, frame_rate = 250, bird_size, pipes_passed = 0;

float pipeSpeed = 1, rect_width;


public void setup(){

  size(800, 600);

  bird = new Bird();
  
  bird_size = bird.get_bird_size() / 2;

  pipes.add(new Pipe(95));
  
  rect_width = pipes.get(0).get_rect_width();

}

public void draw(){
  background(135, 206, 235); // Skyblue background
  bird.update();
  bird.show();
  
  // New pipe draw speed, inverted the original method
  // Numbers for frame_rate based on actual pipe speed below
  if(score > 200){
    frame_rate = 125;
    if(frameCount % frame_rate == 0){
      pipes.add(new Pipe(100));
    }
  }else if(score > 150){
    frame_rate = 142;
    if(frameCount % frame_rate == 0){
      pipes.add(new Pipe(120));
    }
  }
  else if(score > 100){
    frame_rate = 166;
    if(frameCount % frame_rate == 0){
      pipes.add(new Pipe(140));
    }
  }else if(score > 75){
    frame_rate = 200;
    if(frameCount % frame_rate == 0){
      pipes.add(new Pipe(170));
    }
  }else{
    if(frameCount % frame_rate == 0){
      pipes.add(new Pipe(200));
    }
  }

  for(int i = 0; i < pipes.size(); i++){
   if(pipes.get(i).offscreen()){ 
      pipes.remove(pipes.get(i)); 
    }
  }
    
    pipes.get(i).show();
     
    // Create temp variables for each pipe set to check vs bird position
    int tempLeft = pipes.get(i).x;
    int tempRight = tempLeft + pipes.get(i).rect_width;
    float tempTopLip = pipes.get(i).top_lip;
    float tempBottomLip = pipes.get(i).bottom_lip;
    // Check if the bird is in a pipe
    if(bird.x + bird_size > tempLeft && bird.x + bird_size < tempRight){
      if(bird.y - bird_size < tempTopLip || bird.y + 2*bird_size > tempBottomLip){
        // If it is, kill the bird
        bird.killBird();
      }
    }
    pipes.get(i).update();
    // Checking if the bird made it past the pipe
    if(bird.x == pipes.get(i).get_rect_x() + rect_width){
      pipes_passed++;
    }
    textSize(20);
    text("Pipes Passed: " + str(pipes_passed), 10, 50);
  }

  // Add points for time lived
  if(frameCount % 25 == 0){
    score++;
  }

  // Display score or dead
  if(!bird.checkHealth()){
    textSize(20);
    text("Score: " + str(score), 10, 20);
    // Graduated speed if scoreing increases
    if(score > 100){
      this.pipeSpeed = 1.25;
    }
   
    for (Pipe pipe: this.pipes){
      // Set each pipe in list with current speed
      pipe.setSpeed(this.pipeSpeed);
    }
  }
  else{
    textSize(20);
    text("Player Dead!", 10, 20);
    for (Pipe pipe: this.pipes){
      pipe.setSpeed(0);
    }
  }
}

public void keyPressed(){
  // Flap if alive when enter is pressed
  if(!bird.checkHealth()){
    if(key == ENTER){
      bird.flap();
    }
  }
}
