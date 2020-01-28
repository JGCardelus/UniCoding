const frames = 30;

const accel = 48;
const deltaAccel = accel / frames;
const vel = -16;
const jumpTime = accel / Math.abs(vel);

let catusMovement = -10;
let cactusWarning = Math.abs(catusMovement * jumpTime * 4);

/********* PRELOAD  ******/
let dino_run, dino_dead, dino_jump;

function preload() {
  dino_run = loadAnimation('./sprites/mov-1.png', './sprites/mov-2.png');
  dino_dead = loadAnimation('./sprites/dead.png');
  dino_jump = loadAnimation('./sprites/jump.png'); 
}

/****** TIMER *******/
let isOn = false;

let time = 5;
let framesTime = time * 30 * frames;

class Size
{
    constructor(w, h)
    {
        this.w = w;
        this.h = h;
    }
}

const cSize = new Size(700, 500);
const yStart = (cSize.h * 2) / 3;

class Pos
{
    constructor(x, y)
    {
        this.x = x;
        this.y = y;
    }
}

class Cactus
{
    constructor(x)
    {
        this.pos = new Pos(x, yStart);
        this.size = new Size(20, -50);

        this.hasPassedDino = false;
    }

    reset()
    {
        this.pos.x = cSize.w;
        this.pos.y = yStart;
        this.hasPassedDino = false;
    }

    move(deltaX, dino)
    {
        this.pos.x += deltaX;

        if(this.pos.x < 0)
        {
            this.pos.x = cSize.w;
            this.hasPassedDino = false;
        }

        let dinoJump = false;
        if (this.pos.x - dino.pos.x <= cactusWarning)
        {
            if(this.hasPassedDino == false)
            {
                this.hasPassedDino = true;
                dinoJump = true;
            }
        }

        return dinoJump;
    }

    draw()
    {
        fill(0);
        rect(this.pos.x, this.pos.y, this.size.w, this.size.h);
    }
}

class Dinosaur
{
    constructor(x)
    {
        this.pos = new Pos(x, yStart - 45);
        this.size = new Size(50, -90);

        this.isJumping = false;
        //Jumping mechanics yf = y0 + v0t - (gt^2)/2
        this.accel = deltaAccel; 
        this.vel = vel;

        this.startJump = false;
    }

    reset()
    {
        this.pos.x = 0;
        this.pos.y = yStart - 45;
        this.startJump = false;
    }

    move(deltaX)
    {
        this.pos.x += deltaX;

        if (this.startJump == true)
        {
            this.jump();
        }

        if (this.pos.x >= cSize.w)
        {
            isOn = false;
        }
    }

    draw()
    {
        if (this.isJumping)
        {
            animation(dino_jump, this.pos.x, this.pos.y);
        }
        else if (!this.isJumping)
        {
            animation(dino_run, this.pos.x, this.pos.y);
        }
        
        if(!isOn)
        {
            animation(dino_dead, this.pos.x, this.pos.y);
        }
    }

    jump()
    {
        this.pos.y += this.vel;
        this.vel += this.accel;

        if (this.pos.y >= (yStart - 45))
        {
            this.startJump = false;
            this.pos.y = yStart - 45;
            this.vel = vel;
        }
    }
}

let cactus = new Cactus(cSize.w);

let dino = new Dinosaur(0);
let deltaDinoX = cSize.w / framesTime;

function getFramesTime()
{
    framesTime = time * 60 * frames;
    deltaDinoX = cSize.w / framesTime;
}

function setup()
{
    let canvas = createCanvas(cSize.w, cSize.h);
    canvas.parent('canvas');
    frameRate(frames);
}

function draw()
{
    background(255);
    fill(0);
    line(0, (cSize.h * 2) / 3, cSize.w, (cSize.h * 2) / 3);
    if (isOn)
    {
        jump = cactus.move(catusMovement, dino);
        cactus.draw();
        if (jump == true)
        {
            dino.startJump = true;
        }
        dino.move(deltaDinoX, jump);   
    }

    dino.draw();
}