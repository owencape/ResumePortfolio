-- comment

--[[]
    multi line comment

    ]]

-- global variables
hello = 'hello'
-- local variables
local world = 'world!'

--Functions
function sayHello(text)
    print(text)
end

--call a function
sayHello("Hello World!")
--sayHello(hello+world)
sayHello(hello .. world) --concatenation of strings

--conditionals
if world == 'world' then
    print('World')
else
    print('hello!')
end
--while loop count from 10 to 0
local i=10
while i!=0 do 
    i = i -1
    print(i)
end
--for loops from 10 to 0
--for initialize variable, where to stop
for j=10,1,-1 do
    print(j)
end
--repeat (do-while) loop
i=10
repeat 
    i=i-1
    print(i)
until i==0

--Tables are similar to python list

-- one variable with many characteristics
local person = {}
person.name = "ty"
person.age = 87
person.height = 60

--call the information
print(person['name'])
print(person.name)

for key, value in pairs(person) do
    print(key,value)
end