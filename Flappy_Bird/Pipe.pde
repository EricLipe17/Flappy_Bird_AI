public class Pipe{
  private int x, rect_width;
  private float speed, free_space, rect_height, rand_length, top_lip, bottom_lip, min_height;
  
  public Pipe(int gap_In){
    this.x = width;
    this.rect_width = 40;
    this.min_height = height / 6;
    this.rect_height = height / 3;
    this.free_space = gap_In;
    this.speed = 1;
    this.rand_length = random(rect_height);
    this.top_lip = this.min_height + this.rand_length;
    this.bottom_lip = this.top_lip + this.free_space;
  }
  
  public void show(){
    fill(212, 175, 55); // Gold pipes
    rect(this.x, 0, this.rect_width, this.top_lip);
    rect(this.x, this.bottom_lip, this.rect_width, height);
  }
  
  public void update(){
    // Moves pipe by 'speed' distance each tick
    this.x -= this.speed;
  }
  
  public void setSpeed(float newSpeed){
    // Updates pipe speed setting for movement
    this.speed = newSpeed;
  }
  
  public float get_top_lip(){
    // Get method returns value of 'lip' or bottom of top pipe adjacent to gap
    return this.top_lip;
  }
  
  public float get_bottom_lip(){
    // Get method returns value of 'lip' or top of bottom pipe adjacent to gap
    return this.bottom_lip;
  }
}
