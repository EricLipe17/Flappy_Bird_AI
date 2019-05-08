public class Pipe{
  private int speed, x, rect_width;
  private float free_space, rect_height, rand_length, top_lip, bottom_lip, min_height;
  
  public Pipe(){
    this.x = width;
    this.rect_width = 40;
    this.min_height = height / 6;
    this.rect_height = height / 3;
    this.free_space = 85;
    this.speed = 1;
    this.rand_length = random(rect_height);
    this.top_lip = this.min_height + this.rand_length;
    this.bottom_lip = this.top_lip + this.free_space;
  }
  
  public void show(){
    fill(255);
    rect(this.x, 0, this.rect_width, this.top_lip);
    rect(this.x, this.bottom_lip, this.rect_width, height);
  }
  
  public void update(){
    this.x -= speed;
  }
}
