import universal-java-matrix-package;

class NeuralNet{
  // Attributes
  //float pipe_distance, bird_velocity, bird_y_position, pipe_gap, bird_distance_pipe, pipe_velocity;
  private float[] input_features, weights_1, weights_2, biases_1, biases_2;
  
  
  // Constructor
  public NeuralNet(int num_features, int num_weights_1, int num_biases_1){//, int num_weights_2, int num_biases_2){
    this.input_features = new float[num_features];
    this.weights_1 = new float[num_weights_1];
    this.biases_1 = new float[num_biases_1];
    //this.weights_2 = new float[num_weights_2];
    //this.biases_2 = new float[num_biases_2];
  }
  
  
  
  
  // Methods
  public void feedforward(){
    
  }












}
