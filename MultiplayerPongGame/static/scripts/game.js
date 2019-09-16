const player_size = [150, 20];
const canvas_size = [700, 400];

let ball_vel = 10;

class Player
{
    constructor(xo, yo)
    {
        this.x = xo;
        this.y = yo;
        this.w = player_size[0];
        this.h = player_size[1];
    }

    go_center()
    {
        this.y = canvas_size[1] / 2 - this.w / 2;
    }

    is_bouncing()
    {
        if (ball.x <= (this.x + 10) && ball.x >= (this.x - 10)) {
            if (ball.y <= (this.y + 50) && ball.y >= (this.y - 50)) {
              ball.bounce();
            }
        }
    }

    draw()
    {
        noStroke();
        fill(255);
        rect(this.x, this.y, this.h, this.w);
    }
}

class Ball
{
    constructor()
    {
        this.y = 0;
        this.x = 0;
        this.r = 20;

        //Movement
        this.yspeed = 0;
        this.xspeed = ball_vel;
    }

    go_center()
    {
        this.y = canvas_size[1] / 2;
        this.x = canvas_size[0] / 2;
    }

    update()
    {
        this.x = this.x + this.xspeed;
        this.y = this.y + this.yspeed;

        if (this.y < 0) {
            this.yspeed = Math.abs(this.yspeed);
        } 
        else if (this.y > canvas_size[1])
        {
            this.yspeed = this.yspeed * (-1);
        }

        if(this.x < 0)
        {
            this.go_center();
        } 
        else if(this.x > canvas_size[0])
        {
            this.go_center();
        }
    }

    bounce()
    {
        var a = random(-1, 1);
        if (a >= 0) {
            this.yspeed = Math.abs(ball_vel);
        } else {
            this.yspeed = Math.abs(ball_vel) * (-1);
        }
        if (this.xspeed > 0) {
            this.x = this.x - 10;
            this.xspeed = Math.abs(this.xspeed) * (-1);
        } else {
            this.x = this.x + 10;
            this.xspeed = Math.abs(this.xspeed);
        }
    }

    draw()
    {
        noStroke();
        fill(100, 200, 100);
        ellipse(this.x, this.y, this.r, this.r);
    }
}

let player_a = new Player(10, 0);
let player_b = new Player(canvas_size[0] - 60, 0);

let ball = new Ball();

function setup()
{
    createCanvas(canvas_size[0], canvas_size[1]);
    background(0);   
    frameRate(30);

    player_a.go_center();
    player_b.go_center();
    ball.go_center();
}

function draw()
{
    background(0)
    ball.update();
    ball.draw();
    
    player_a.is_bouncing();
    player_a.draw();

    player_b.is_bouncing();
    player_b.draw();
}