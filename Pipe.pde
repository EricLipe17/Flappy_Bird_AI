public class Pipe{
  private int x, rect_width, speed;
  private float free_space, rect_height, rand_length;
  
  public Pipe(){
    this.x = width;
    this.rect_width = 40;
    this.rect_height = height / 3;
    this.free_space = 75;
    this.speed = 2;
    this.rand_length = random(height / 3);
  }
  
  public void show(){
    fill(255);
    rect(this.x, 0, this.rect_width, this.rect_height);
    rect(this.x, this.rect_height + this.rand_length + this.free_space, this.rect_width, height);
  }
  
  
  public void update(){
    this.x -= speed;
  }
  
  public boolean offscreen(){
    if(this.x + this.rect_width < 0){
      return true;
    }
    return false;
  }
  
  public boolean hit(Bird bird){
    if((bird.y <= this.rect_height && bird.x + 6 == this.x) || (bird.y > this.rect_height + this.rand_length + this.free_space && bird.x + 6 == this.x)){
      noLoop();
      return true;
    }
    return false;
  }
}
