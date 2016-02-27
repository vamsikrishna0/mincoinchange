#A minimum coin change application in python web-app

import webapp2
from google.appengine.api import memcache
from google.appengine.api import users

def min_change(s, p):
    V = [int(i) for i in s.split()]
    C = int(p)
    m, n = len(V)+1, C+1

    for p in range(n):
      for q in range (m):
        memcache.set(str(p)+str(q), 0)
    for j in xrange(1, n):
        memcache.set(str(0)+str(j), float('inf'))
       
    for i in xrange(1, m):
        for j in xrange(1, n):
            if j - V[i-1] >= 0:
              ac = memcache.get(str(i)+str(j - V[i-1]))
            else:
              ac = float('inf')
            memcache.set(str(i)+str(j), min(memcache.get(str(i-1)+str(j)), 1 + ac))
          
    ret = memcache.get(str(m-1)+str(n-1))
    memcache.flush_all()
    return ret

class MainPage(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()

    if user:
      self.response.out.write('<html><body><h3>Hello ')
      self.response.out.write(user.nickname() + '</h3>')
      self.response.out.write('<a href="' + users.create_logout_url('/'))
      self.response.out.write('">Logout</a><br>')
      if 'v' in self.request.GET.keys() and 'c' in self.request.GET.keys():
        self.response.out.write('The coins :'+ self.request.GET['v'] + '<br> The amount :' + self.request.GET['c']+'<br>')
        self.response.out.write('Min number of coins = '+ str(min_change(self.request.GET['v'], self.request.GET['c'])))
      self.response.out.write('<form method="GET">')  
      self.response.out.write('<h4>Enter the different coin denominations (separated by spaces)</h4>')
      self.response.out.write('<input name="v" type="text">')
      self.response.out.write('<h4>Enter the change for which min coins has to be detrmined</h4>')
      self.response.out.write('<input name="c" type="text">')
      self.response.out.write('<input type="submit">')
      self.response.out.write('</body></html>')
    else:
      self.response.out.write('<a href="' + users.create_login_url('/'))
      self.response.out.write('">Login</a>')
    

app = webapp2.WSGIApplication([
  ('/', MainPage)
], debug=True)
