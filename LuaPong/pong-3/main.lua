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
end

function love.update(dt)
    if love.keyboard.isDown('w')then
        player1Y = player1Y + -PADDLE_SPEED*dt 
    elseif love.keyboard.isDown('s')then
        player1Y = player1Y + PADDLE_SPEED*dt
    end
    if love.keyboard.isDown('up')then
        player2Y = player2Y + -PADDLE_SPEED*dt 
    elseif love.keyboard.isDown('down')then
        player2Y = player2Y + PADDLE_SPEED*dt
    end

end


function love.keypressed(key)
    if key =='escape' then
        love.event.quit()
    end
end
--called after update function by Love2d, this draws what is on your screen
function love.draw()
    --begin rendering a virtual res
    push:apply('start')


    love.graphics.clear(40,45,52,255)
    love.graphics.printf(
        'Hello Pong!',0,20,VIRTUAL_WIDTH,'center')  
    
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
        
    love.graphics.rectangle('fill',10,player1Y,5,20)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH-10,player2Y,5,20)
    love.graphics.rectangle('fill',VIRTUAL_WIDTH/2,VIRTUAL_HEIGHT/2,4,4)
    --end rendering
    push:apply('end')
end
