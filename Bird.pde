public class Bird{
  private int x, y;
  private float velocity, gravity, flap_force;
  
  public Bird(){
    this.x = 50;
    this.y = height/2;
    this.gravity = 0.6;
    this.velocity = 0;
    this.flap_force = 14;
  }
  
  public void show(){
    fill(255);
    ellipse(this.x, this.y, 20, 20);
  }
  
  public void update(){
    if(this.y >= height){
      this.y = height;
      this.velocity = 0;
    }

    this.velocity += gravity;
    this.velocity *= 0.95;
    this.y += this.velocity;
  }
  
  public void flap(){
    this.velocity -= this.flap_force;
  }
}
