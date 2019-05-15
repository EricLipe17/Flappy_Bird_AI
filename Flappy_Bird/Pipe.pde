public class Pipe{
  // Attributes

  private int x, rect_width;

  private float speed, free_space, rect_height, rand_length, top_lip, bottom_lip, min_height;
  
  private PImage up_pipe, down_pipe;



  public Pipe(int gap_In){
    // Pipe constructor

    this.x = width;

    this.rect_width = 40;

    this.min_height = height / 6;

    this.rect_height = height / 3;

    this.free_space = gap_In;

    this.speed = 1;

    this.rand_length = random(rect_height);

    this.top_lip = this.min_height + this.rand_length;

    this.bottom_lip = this.top_lip + this.free_space;
    
    this.up_pipe = loadImage("pipe_two_way_1000px.png");
    
    this.down_pipe = loadImage("pipe_two_way_1000px.png");

  }

  

  public void show(){
    // Displays the up and down pipe sprites to the sketch
    image(this.down_pipe, this.x, this.top_lip - 1000);
    
    // Something is wrong with the 'up_pipe' when it is displayed.
    image(this.up_pipe, this.x, this.bottom_lip);
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
  
  
  
   public boolean offscreen(){ 
    // Determines whether or not the pipe object is off of the screen
    if(this.x + this.rect_width < 0){ 
      return true; 
    } 
    return false; 
   }
   
   
   
   public int get_rect_width(){
     // Get method returns the pipes width
     return this.rect_width;
   }
   
   
   
   public int get_rect_x(){
     // Get method returns the pipes x coordinate
     return this.x;
   }
}
