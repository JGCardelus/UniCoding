const frames = 15;

class Size
{
    constructor(w, h)
    {
        this.w = w;
        this.h = h;
    }
}

class Pos
{
    constructor(x, y)
    {
        this.x = x;
        this.y = y;
    }
}

class Obj
{
    constructor(x)
    {
        this.pos = new Pos(x, (cSize.h * 2) / 3)
        this.size = new Size(20, -50);

        this.isJumping = false;
        //Jumping mechanics yf = y0 + v0t - (gt^2)/2
        this.accel = -9.8 / frames; 

        this.hasJumped = false;
    }

    move(deltaX)
    {
        this.pos.x += deltaX;
    }

    draw()
    {
        fill(0);
        rect(this.pos.x, this.pos.y, this.size.w, this.size.h);
    }

    jump(cactus)
    {
        if ((x_cactus - this.x) < 10)
        {
            console.log("Salta");
            hasJumped = true;
        }
    }
}

let cSize = new Size(700, 500);
let cactus = new Obj(cSize.w);
let classTime = 1 * 30 * frames;

let dino = new Obj(0);
let deltaDinoX = cSize.w / classTime;



function setup()
{
    createCanvas(cSize.w, cSize.h);
    frameRate(frames);
}

function draw()
{
    background(255);
    fill(0);
    line(0, (cSize.h * 2) / 3, cSize.w, (cSize.h * 2) / 3);
    cactus.move(-6);
    cactus.draw();
    dino.move(deltaDinoX);
    dino.draw();
}