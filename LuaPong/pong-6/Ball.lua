Ball = Class{}

--def__init__(self): Constructor
function Ball:init(x,y,width,height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.dx = math.random(2) == 1 and -100 or 100
    self.dy = math.random(-50, 50)
end

--reset the ball
function Ball:reset()
    self.x = VIRTUAL_WIDTH / 2 - 2
    self.y = VIRTUAL_HEIGHT / 2 - 2
    self.dx = math.random(2) == 1 and 100 or -100 --HOW TO HELP CONTROL WHO GETS BALL SERVED TO THEM
    self.dy = math.random(-50,50) * 1.5
end

--update the ball
function Ball:update(dt)
    self.x = self.x + self.dx * dt
    self.y = self.y + self.dy * dt


end


--draw the ball onto the screen
function Ball:render()
    love.graphics.rectangle('fill',self.x,self.y,self.width,self.height)
end