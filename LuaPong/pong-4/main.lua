--[[
    Love2d looks for main functions 
     it has a certain order that the program HAS TO run

]]

push = require 'push'
--screen ratio 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200
player1Y= 30
player2Y = VIRTUAL_HEIGHT-50
player1Score=0
player2Score=0

--runs when the game first starts up, only once... ONLY ONCE
function love.load()
    -- nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics
    love.graphics.setDefaultFilter('nearest','nearest')

    --set the seed of the serve
    math.randomseed(os.time())

    --more retro font
    smallFont=love.graphics.newFont('font.ttf',8)
    scoreFont=love.graphics.newFont('font.ttf',32)
    --set font to retro look
    love.graphics.setFont(smallFont)
    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })

    ballX = VIRTUAL_WIDTH / 2 - 2
    ballY = VIRTUAL_HEIGHT / 2 - 2
    ballDX = math.random(2) == 1 and 100 or -100 --HOW TO HELP CONTROL WHO GETS BALL SERVED TO THEM
    ballDY = math.random(-50,50)
    gameState='start'
end

function love.update(dt)
    if love.keyboard.isDown('w')then
        player1Y = math.max(0, player1Y + -PADDLE_SPEED*dt)
         
    elseif love.keyboard.isDown('s')then
        player1Y = math.min(VIRTUAL_HEIGHT - 20, player1Y + PADDLE_SPEED*dt)
    end
    if love.keyboard.isDown('up')then
        player2Y = math.max(0, player2Y + -PADDLE_SPEED*dt)
    elseif love.keyboard.isDown('down')then
        player2Y = math.min(VIRTUAL_HEIGHT - 20, player2Y + PADDLE_SPEED*dt)
    end

    if gameState == 'play' then


        ballX=ballX+ballDX*dt
        ballY=ballY+ballDY*dt
    end
        

end


function love.keypressed(key)
    if key =='escape' then
        love.event.quit()
    elseif key=='enter' or key=='return' then
        if gameState == 'start' then
            gameState = 'play'
        else
            gameState = 'start'
        

            --reset ball
            ballX = VIRTUAL_WIDTH / 2 - 2
            ballY = VIRTUAL_HEIGHT / 2 - 2
            ballDX = math.random(2) == 1 and 100 or -100 --HOW TO HELP CONTROL WHO GETS BALL SERVED TO THEM
            ballDY = math.random(-50,50)
        end

    end
end
--called after update function by Love2d, this draws what is on your screen
function love.draw()
    --begin rendering a virtual res
    push:apply('start')


    love.graphics.clear(40,45,52,255)
    if gameState == 'start' then
        love.graphics.printf('Hello Start State!',0,20,VIRTUAL_WIDTH,'center')  
    else
        love.graphics.printf('Hello Play State!',0,20,VIRTUAL_WIDTH,'center')  
    end
    
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
        
    love.graphics.rectangle('fill',10,player1Y,5,20)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)
    love.graphics.rectangle('fill',ballX,ballY,4,4)
    --end rendering
    push:apply('end')
end
