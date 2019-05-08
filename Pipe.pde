public class Pipe{
  private int speed, x, rect_width;
  private float free_space, rect_height, rand_length;
  
  public Pipe(){
    this.x = width;
    this.rect_width = 40;
    this.rect_height = height / 3;
    this.free_space = 85;
    this.speed = 1;
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
}
