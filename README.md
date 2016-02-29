# Crime-Scene-Investigator
This application uses projective transformation. 
The idea is similar to what is used in some crime scene investigation models, but this one works in 2D (meaning on flat surfaces).

### Usage
Let's suppose, the red area is restricted. Nobody is allowed to sail here. 


![alt text][area]

We have this picture of a boat, but it was taken in an angle so it is hard to determine whether it is in the specific area or not.


<img src="https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/assets/angle_pic.jpg" width="640">

By using the application, we can solve this problem easily. First we select 4 points (so that no three of them are collinear). 
Then we select the same 4 on the other picture. Given these conditions, we can determine any point's location on the other picture.


![alt text][boat_gif]


 We can conclude that the ship is in the area.
 
### Another Example
This time not from above, just from 2 different angles. We can still see how the red dot moves simultaneously on the other pictures.


<img src="https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/read_me/table.gif" width="800">



[boat_gif]: https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/read_me/boat.gif "Is the boat in the restricted area?"
[table]: https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/read_me/table.gif "Table"
[area]: https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/assets/top_pic.jpg "Restricted area"
[boat]: https://github.com/LengyelR/Crime-Scene-Investigator/blob/master/assets/angle_pic.jpg "Suspected boat"
