--[[
    Love2d looks for main functions 
     it has a certain order that the program HAS TO run

]]

--screen ratio 16:9
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

--runs when the game first starts up, only once... ONLY ONCE
function love.load()
    love.window.setMode(WINDOW_WIDTH,WINDOW_HEIGHT,{
        fullscreen = false,
        resizable = false,
        vsync = true})

end

function love.update()
end

--called after update function by Love2d, this draws what is on your screen
function love.draw()
    love.graphics.printf(
        'Hello Pong!',              --text to render
        0,                          --starting X location
        WINDOW_HEIGHT/2 - 6,        --starting Y location
        WINDOW_WIDTH,               --numbers of pixels to center within
        'center')                   --center allign
end
