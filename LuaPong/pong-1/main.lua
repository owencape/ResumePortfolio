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
--runs when the game first starts up, only once... ONLY ONCE
function love.load()
    -- nearest-nearest filtering on upscaling and downscaling to prevent blurring of text and graphics
    love.graphics.setDefaultFilter('nearest','nearest')

    push:setupScreen(VIRTUAL_WIDTH,VIRTUAL_HEIGHT,WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen=false,
        resizable=false,
        vsync=true
    })
end

function love.update()
end

--called after update function by Love2d, this draws what is on your screen
function love.draw()
    --begin rendering a virtual res
    push:apply('start')


    love.graphics.printf(
        'Hello Pong!',              --text to render
        0,                          --starting X location
        VIRTUAL_HEIGHT/2 - 6,        --starting Y location
        VIRTUAL_WIDTH,               --numbers of pixels to center within
        'center')                   --center allign

    --end rendering
    push:apply('end')
end
