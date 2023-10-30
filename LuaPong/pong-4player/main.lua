--[[
    Love2d looks for main functions 
     it has a certain order that the program HAS TO run

]]
Class = require 'class'
push = require 'push'
require 'Ball'
require 'Paddle'

--screen ratio 1:1
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 720

VIRTUAL_WIDTH = 243
VIRTUAL_HEIGHT = 243

PADDLE_SPEED = 200
player1= Paddle(7,30,5,20)
player2= Paddle(VIRTUAL_WIDTH-7,VIRTUAL_HEIGHT-30,5,20)
player4= Paddle(30,7,20,5)
player3= Paddle(VIRTUAL_HEIGHT-30,VIRTUAL_WIDTH-7,20,5)
player1Score=1
player2Score=1
player3Score=1
player4Score=1



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
-- keyboard setup
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
    if love.keyboard.isDown('a')then
        player4.dx=-PADDLE_SPEED
    elseif love.keyboard.isDown('d')then
        player4.dx=PADDLE_SPEED
    else
        player4.dx=0
    end
    if love.keyboard.isDown('left')then
        player3.dx=-PADDLE_SPEED
    elseif love.keyboard.isDown('right')then
        player3.dx=PADDLE_SPEED
    else
        player3.dx=0
    end

    if gameState =='serve' then
        collidedWith = servingPlayer
        --before switching to play, need to set ball velocity
        if servingPlayer == 1 then
            ball.dx = math.random(140,200)
            ball.dy = math.random(-50,50)
        elseif servingPlayer ==2 then
            ball.dx = -math.random(140,200)
            ball.dy = math.random(-50,50)
        elseif servingPlayer ==3 then
            ball.dy = math.random(140,200)
            ball.dx = math.random(-50,50)
        else
            ball.dy = -math.random(140,200)
            ball.dx = math.random(-50,50)
        end
        
    elseif gameState == 'play' then
        -- paddle collisions
        if ball:collides(player1)then
            ball.dx = -ball.dx * 1.03
            ball.x = player1.x+5
            collidedWith = 1
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
            collidedWith = 2
            if ball.dy<0 then 
                ball.dy= - math.random(10,150)
            else
                ball.dy = math.random(10,150)
            end
            sounds['paddle_hit']:play()
    
        end

        if ball:collides(player4)then
            ball.dx = -ball.dx * 2.03
            ball.y = player4.y+5
            collidedWith = 4
            if ball.dy<0 then 
                ball.dy=  math.random(10,150)
            else
                ball.dy = - math.random(10,150)
            end
            sounds['paddle_hit']:play()
    
        end

        if ball:collides(player3)then
            ball.dx = -ball.dx * 0.75
            ball.y = player3.y-5
            collidedWith = 3
            if ball.dy<0 then 
                ball.dy= math.random(10,150)
            else
                ball.dy = - math.random(10,150)
            end
            sounds['paddle_hit']:play()
    
        end
        -- informs that if ball passes border this is a serve
        
        if ball.y <0 then
            gameState = 'serve'
        end
        if ball.y > VIRTUAL_HEIGHT then 
            gameState = 'serve'
        end

        -- ball:update(dt)
        -- gets who was the person who scored the point so the point is added to their score
        if (ball.x <0) or (ball.x > VIRTUAL_WIDTH) or (ball.y <0) or (ball.y > VIRTUAL_HEIGHT) then
            if collidedWith == 1 then
                player1Score = player1Score + 1
            elseif collidedWith == 2 then
                player2Score = player2Score + 1
            elseif collidedWith == 3 then
                player3Score = player3Score + 1
            else
                player4Score = player4Score + 1
            end
        end

        -- boundaries to keep track of score
        if ball.x < 0 then
            player1Score = player1Score - 1
            sounds['score']:play()
            if player1Score==0 then
                losingPlayer=1
                gameState='done'
            else
                servingPlayer = 1
                ball:reset()
                gameState='serve'
            end

        end
        
        if ball.x > VIRTUAL_WIDTH then
            player2Score = player2Score - 1
            sounds['score']:play()
            if player2Score == 0 then
                losingPlayer=2
                gameState='done'
            else
                servingPlayer = 2
                ball:reset()
                gameState='serve'
            end
            
        end
        if ball.y< 0 then
            player3Score = player3Score - 1
            sounds['score']:play()
            if player3Score==0 then
                losingPlayer=3
                gameState='done'
            else
                servingPlayer = 3
                ball:reset()
                gameState='serve'
            end
            
        end
        if ball.y > VIRTUAL_HEIGHT - 10 then
            player4Score = player4Score - 1
            sounds['score']:play()
            if player4Score==0 then
                losingPlayer=4
                gameState='done'
            else
                servingPlayer = 4
                ball:reset()
                gameState='serve'
            end
        end
        ball:update(dt)
    end
    player1:update(dt,1)
    player2:update(dt,2)
    player3:update(dt,3)
    player4:update(dt,4)
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
            player1Score=7
            player2Score=7
            player3Score=7
            player4Score=7
            ball:reset()
            -- serving algorithm
            if losingPlayer ==1 then
                servingPlayer=2
            elseif losingPlayer == 2 then
                servingPlayer = 3
            elseif losingPlayer == 3 then
                servingPlayer = 4
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
    love.graphics.setColor(255,0,0)
    love.graphics.print(tostring(player1Score), VIRTUAL_WIDTH / 2 - 50, VIRTUAL_HEIGHT / 3)
    love.graphics.setColor(255,255,0)
    love.graphics.print(tostring(player3Score), VIRTUAL_WIDTH / 2 + 30, VIRTUAL_HEIGHT / 3)
    love.graphics.setColor(0,255,0)
    love.graphics.print(tostring(player2Score), VIRTUAL_WIDTH / 2 +30, VIRTUAL_HEIGHT / 1.75)
    love.graphics.setColor(0,0,255)
    love.graphics.print(tostring(player4Score), VIRTUAL_WIDTH / 2 -50, VIRTUAL_HEIGHT / 1.75)
    love.graphics.setColor(255,255,255)
    
    -- scoreboard
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
            love.graphics.printf('Player ' .. tostring(losingPlayer) .. ' loses!',
                0, 10, VIRTUAL_WIDTH, 'center')
            love.graphics.setFont(smallFont)
            love.graphics.printf('Press Enter to restart!', 0, 30, VIRTUAL_WIDTH, 'center')
    end
    -- colors
    love.graphics.setColor(255,0,0)
    player1:render()
    love.graphics.setColor(0,255,0)
    player2:render()
    love.graphics.setColor(0,0,255)
    player3:render()
    love.graphics.setColor(255,255,0)
    player4:render()
    love.graphics.setColor(255,255,255)
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

function love.resize(w, h)
    push:resize(w, h)
end
