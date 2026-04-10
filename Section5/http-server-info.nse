description = [[
Simple HTTP server info script
]]

author = "Student"

categories = {"default"}

portrule = function(host, port)
  return port.number == 80 or port.number == 8080
end

action = function(host, port)
  return "HTTP service detected on port " .. port.number
end