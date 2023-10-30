--[[
    Love2d looks for main functions 
     it has a certain order that the program HAS TO run

]]
Class = require 'class'
push = require 'push'
require 'Ball'
require 'Paddle'

--screen ratio 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200
player1= Paddle(10,30,5,20)
player2= Paddle(VIRTUAL_WIDTH-10,VIRTUAL_HEIGHT-30,5,20)
player1Score=0
player2Score=0

--runs when the game first starts up, only once... ONLY ONCE
function love.load()
    -- nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics
    love.graphics.setDefaultFilter('nearest','nearest')

    love.window.setTitle('Pong')

    --set the seed of the serve
    math.randomseed(os.time())

    --more retro font
    smallFont=love.graphics.newFont('font.ttf',8)
    scoreFont=love.graphics.newFont('font.ttf',32)
    largeFont=love.graphics.newFont('font.ttf',16)
    --set font to retro look
    love.graphics.setFont(smallFont)


    sounds = {
        ['paddle_hit'] = love.audio.newSource('sounds/paddle_hit.wav','static'),
        ['score'] = love.audio.newSource('sounds/score.wav','static'),
        ['wall_hit'] = love.audio.newSource('sounds/wall_hit.wav','static')

    }




    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })

    ball = Ball(VIRTUAL_WIDTH/2-2,VIRTUAL_HEIGHT/2-2,4,4)


    gameState='start'
end

function love.update(dt)
    if love.keyboard.isDown('w')then
        player1.dy=-PADDLE_SPEED
         
    elseif love.keyboard.isDown('s')then
        player1.dy=PADDLE_SPEED
    else
        player1.dy=0
    end
    if love.keyboard.isDown('up')then
        player2.dy=-PADDLE_SPEED
    elseif love.keyboard.isDown('down')then
        player2.dy=PADDLE_SPEED
    else
        player2.dy=0
    end
    if gameState =='serve' then
        --before switching to play, need to set ball velocity
        if servingPlayer == 1 then
            ball.dx = math.random(140,200)
        else
            ball.dx = -math.random(140,200)
        end
        ball.dy = math.random(-50,50)
    elseif gameState == 'play' then

        if ball:collides(player1)then
            ball.dx = -ball.dx * 1.03
            ball.x = player1.x+5

            if ball.dy<0 then 
                ball.dy= - math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
            sounds['paddle_hit']:play()
        end

        if ball:collides(player2)then
            ball.dx = -ball.dx * 1.03
            ball.x = player2.x-5

            if ball.dy<0 then 
                ball.dy= - math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
            sounds['paddle_hit']:play()
    
        end
        --wall collision
        if ball.y <=0 then
            ball.y=0
            sounds['wall_hit']:play()
            ball.dy = -ball.dy
        end
        if ball.y>=VIRTUAL_HEIGHT-4 then
            ball.y = VIRTUAL_HEIGHT-4
            sounds['wall_hit']:play()
            ball.dy = -ball.dy
        end



        ball:update(dt)
    end


    if ball.x < 0 then
        player2Score = player2Score + 1
        sounds['score']:play()
        servingPlayer = 2
        if player2Score==3 then
            winningPlayer=2
            gameState='done'
        else
        
            gameState='serve'
        end
        ball:reset()

    end
    
    if ball.x > VIRTUAL_WIDTH then
        player1Score = player1Score + 1
        sounds['score']:play()
        servingPlayer = 1
        if player1Score==3 then
            winningPlayer=1
            gameState='done'
        else
            
            gameState='serve'
        end
        ball:reset()

    end





    player1:update(dt)
    player2:update(dt)


        

end


function love.keypressed(key)
    if key =='escape' then
        love.event.quit()
    elseif key=='enter' or key=='return' then
        if gameState == 'start' then
            gameState = 'serve'
        elseif gameState =='serve'then
            gameState='play'
        elseif gameState=='done' then
            gameState='serve'
            player1Score=0
            player2Score=0
            ball:reset()
            if winningPlayer ==1 then
                servingPlayer=2
            else
                servingPlayer=1
            end
            
        
        

            --reset ball
            
        end

    end
end
--called after update function by Love2d, this draws what is on your screen
function love.draw()
    --begin rendering a virtual res
    push:apply('start')


    love.graphics.clear(40,45,52,255)
    love.graphics.setFont(smallFont)

    
    love.graphics.setFont(scoreFont)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)

    if gameState == 'start' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Welcome to Pong!', 0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to begin!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'serve' then
        love.graphics.setFont(smallFont)
        love.graphics.printf('Player ' .. tostring(servingPlayer) .. "'s serve!", 
            0, 10, VIRTUAL_WIDTH, 'center')
        love.graphics.printf('Press Enter to serve!', 0, 20, VIRTUAL_WIDTH, 'center')
    elseif gameState == 'play' then
        -- no UI messages to display in play
    elseif gameState == 'done' then
        love.graphics.setFont(largeFont)
            love.graphics.printf('Player ' .. tostring(winningPlayer) .. ' wins!',
                0, 10, VIRTUAL_WIDTH, 'center')
            love.graphics.setFont(smallFont)
            love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')
    end
        
    player1:render()
    player2:render()
    ball:render()
    displayFPS()
    --end rendering
    push:apply('end')
end


function displayFPS()
    -- simple FPS display across all states
    love.graphics.setFont(smallFont)
    love.graphics.setColor(0, 255, 0, 255)
    love.graphics.print('FPS: ' .. tostring(love.timer.getFPS()), 10, 10)
end
