public class Bird{
  // Attributes

  private int x, y, bird_size, img_size;

  private float velocity, gravity, flap_force;

  private boolean isDead = false;
  
  private PImage bird_img;

  

  public Bird(){
    // Bird constructor

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
    // Displays the Flappy Bird sprite in the sketch
    image(bird_img, this.x - 125, this.y - 125, img_size, img_size);
  }

  

  public void update(){
    // Updates the birds y-position based on gravity
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
    // Updates the birds position based on the strength of the flap force
    this.velocity -= this.flap_force;
  }

  

  public boolean checkHealth(){
    // Get method returns status of bird
    return isDead;
  }

  

  public void killBird(){
    // Sets the birds life status to dead
    isDead = true;
  }
  
  
  
  public int get_bird_size(){
    // Get method returns birds size
    return this.bird_size;
  }
}
