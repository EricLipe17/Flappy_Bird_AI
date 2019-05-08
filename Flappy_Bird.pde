
Bird bird;
ArrayList<Pipe> pipes = new ArrayList<Pipe>();

public void setup(){
  size(800, 600);
  bird = new Bird();
  pipes.add(new Pipe());
}

public void draw(){
  background(0); //<>//
  bird.update();
  bird.show(); //<>//
  bird.is_dead();
  
  if(frameCount % 150 == 0){
      pipes.add(new Pipe());
  }
  
  for(int i = 0; i < pipes.size(); i++){
    pipes.get(i).show();
    pipes.get(i).update();
    if(pipes.get(i).hit(bird)){
      println("hit");
    }
    if(pipes.get(i).offscreen()){
      pipes.remove(pipes.get(i));
    }
    println(pipes.size());
  }
} //<>//

public void keyPressed(){
  if(key == ENTER){
    bird.flap();
  }
}
