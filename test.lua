local function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

--file = io.open('wsgi.py')
--print(file:read())
--print(file:read())
--print(file:read())
--print(file:read())
--print(file:read())

if request.method == 'POST' then
    data = request.form
else
    data = request.query
end

-- return debug.getinfo(inspect)

--return inspect(data)

return string.format([[
<html>
<body>
<h1>Hello world</h1>
<textarea cols="50" rows="5">%s</textarea>
</body>
</html>
]], dump(data))
