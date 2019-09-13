const player_size = [100, 50];
const canvas_size = [700, 400];

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
        this.y = canvas_size[0] / 2 + this.w / 2;
    }

    draw()
    {
        noStroke()
        fill(100, 100, 100)
        rect(this.x, this.y, this.w, this.h)
    }
}


let player_a = Player();
let player_b =

function setup()
{
    createCanvas(canvas_size[0], canvas_size[1]);
    background(20);

    frameRate(30)
}

function draw()
{

}