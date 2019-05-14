public class Bird{

  private int x, y, bird_size, img_size;

  private float velocity, gravity, flap_force;

  private boolean isDead = false;
  
  private PImage bird_img;

  

  public Bird(){

    this.x = 50;

    this.y = height/2;

    this.gravity = 0.6;

    this.velocity = 0;

    this.flap_force = 14;
    
    this.bird_size = 20;
    
    this.bird_img = loadImage("flappy_free.png");
    
    this.img_size = 250;

  }

  

  public void show(){
    if(!isDead){
      fill(255, 255, 0);
    }
    else{
      fill(255, 0, 0);
    }
    ellipse(this.x, this.y, bird_size, bird_size);
    image(bird_img, this.x - 125, this.y - 125, img_size, img_size);
  }

  

  public void update(){
    if(this.y >= height){
      this.y = height;
      this.velocity = 0;
      isDead = true;
    }
    else if(this.y <= 0){
      isDead = true; 
    }
    this.velocity += gravity;
    this.velocity *= 0.95;
    this.y += this.velocity;
  }

  

  public void flap(){
    this.velocity -= this.flap_force;
  }

  

  public boolean checkHealth(){
    return isDead;
  }

  

  public void killBird(){
    isDead = true;
  }
  
  
  
  public int get_bird_size(){
    return this.bird_size;
  }
}
