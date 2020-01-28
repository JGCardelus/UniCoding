
let cSize = [800, 500];
let paPoints = 0;
let pbPoints = 0;


class Ball
{
    constructor()
    {
        this.x = cSize[0] / 2;
        this.y = cSize[1] / 2;

        this.r = 30;

        this.accel_x = 15;
        this.accel_y = 15;

        this.vel_x = 0;
        this.vel_y = 0;
    }

    reset()
    {
        this.x = cSize[0] / 2;
        this.y = cSize[1] / 2;

        this.accel_x = 15;
        this.accel_y = 15;

        this.vel_x = 0;
        this.vel_y = 0;
    }

    move(player_a, player_b)
    {
        //Check bounds
        if ((this.y + this.r) > cSize[1])
        {
            this.accel_y *= -1 * Math.random();
            this.y = cSize[1] - this.r;
        }
        if((this.y - this.r) < 0)
        {
            this.accel_y *= -1  * Math.random();
            this.y = this.r;
        }

        if((this.x + this.r) > cSize[0])
        {
            paPoints += 1;
            print("Player A: " + paPoints)
            this.reset();
        }
        if((this.x - this.r) < 0)
        {
            pbPoints += 1;
            print("Player B: " + pbPoints)
            this.reset();
        }

        if((this.y + this.r) <= (player_b.y + player_b.h) && (this.y - this.r) >= player_b.y)
        {
            if((this.x + this.r) >= player_b.x)
            {
                this.accel_x *= -1;
            }
        }
        
        if((this.y + this.r) <= (player_a.y + player_a.h) && (this.y - this.r) >= player_a.y)
        {
            if((this.x - this.r) <= player_a.x)
            {
                this.accel_x *= -1;
            }
        }

        this.vel_x = this.accel_x;
        this.vel_y = this.accel_y;

        this.x += this.vel_x;
        this.y += this.vel_y;
    }

    draw()
    {
        ellipseMode(CENTER);
        fill(200, 0, 0);
        ellipse(this.x, this.y, this.r, this.r)
    }
}

class Player
{
    constructor(x)
    {
        this.x = x;
        this.w = 30;
        this.h = 150; 

        this.y = cSize[1] / 2 - this.h / 2;

        this.accel = 0;
        this.vel = 0;
        this.max_accel = 30;
    }

    reset()
    {
        this.y = cSize[1] / 2 - this.h / 2;
    }

    move()
    {
        /*
        if (this.vel >= -0.70 && this.vel <= 0.70)
        {
            console.log("Too small");
            this.accel = 0;
            this.vel = 0;
        }
        */
        let next_y = this.y + this.vel;

        if (next_y < 0)
        {
            next_y = 0;
        }
        
        if((next_y + this.h) > cSize[1])
        {
            next_y = cSize[1] - this.h;
        }

        this.y = next_y;
    }

    draw()
    {
        fill(200, 0, 200);
        rect(this.x, this.y, this.w, this.h);
    }
}

let playing = true;

function setup()
{
    createCanvas(800, 500);
    background(0);
    
    frameRate(30);
}

let ball = new Ball();
let player_a = new Player(10);
let player_b = new Player(cSize[0] - 10 - 30);

function draw()
{
    background(0);
    if (playing == true)
    {
        
        if (!keyIsDown(DOWN_ARROW) && !keyIsDown(UP_ARROW) && player_b.accel != 0)
        {
            player_b.vel = 0;
        }
        if (!keyIsDown(83) && !keyIsDown(87) && player_a.accel != 0)
        {
            player_a.vel = 0;
        }
        
        //Something
        player_a.move();
        player_b.move();
        ball.move(player_a, player_b);
    }
    ball.draw();
    player_a.draw();
    player_b.draw();
}

function keyPressed()
{
    if(playing == true)
    {
        console.log("Key Pressed");
        if(keyCode == DOWN_ARROW)
        {
            player_b.vel = 20;
        }
        else if(keyCode == UP_ARROW)
        {
            player_b.vel = -20;
        }
        
        
        if(keyCode == 83)
        {
            player_a.vel = 20;
        }
        else if(keyCode == 87)
        {
            player_a.vel = -20;
        }   
    }
}