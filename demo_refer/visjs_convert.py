import sys

def main():
    '''
    -e http.host -e http.request.uri   -e http.referer  -e http.location
   ww.c5.ybosrcqo.us|/|
   www.msltb.com|/addons/theme/images/tavd.jpg|http://www.msltb.com/addons/moban1.asp?id=a1-14754&abn=&xxf=0
    
    var nodes = new vis.DataSet([
    {id: '1', label: 'Node 1'},
    {id: 2, label: 'Node 2'},
    {id: 3, label: 'Node 3'},
    {id: 4, label: 'Node 4'},
    {id: 5, label: 'Node 5'}
  ]);

  // create an array with edges
  var edges = new vis.DataSet([
    {from: '1', to: 3},
    {from: '1', to: 2},
    {from: 2, to: 4},
    {from: 2, to: 5},
    {from: 3, to: 3}
  ]);    
    
    '''
    nodes = {}
    edges = set()
    prev_info = ()
    with open(sys.argv[1]) as fr:
        for line in fr:
            line = line.replace('http://', '', 1).replace('https://', '', 1)
            host, uri, ref, location = line.strip().split('|')
            if not ref and not location:
                continue
                        
            ref_host, sep, ref_uri = ref.partition('/')
            ref_uri = sep + ref_uri
            
            if location:
                #others must be empty
                #www.tjhuajiantang.com|/?id=a1-14754&xxf=0|http://syndication.exoclick.com/splash.php?cat=&idzone=2140479&type=8&p=http%3A%2F%2Fxlxtube.com%2F&sub=|  this contains the prev_info
                #|||http://www.msltb.com/addons/moban1.asp?id=a1-14754&abn=&xxf=0
                try:
                    ref_host, ref_uri, host, uri = prev_info
                except:
                    continue
                
                #need to overwrite host, uri by location
                host, sep, uri = location.partition('/')
                uri = sep + uri
                
            nodes[host] = 'host'
            nodes[uri] = 'uri'
            nodes[ref_host] = 'ref_host'
            nodes[ref_uri] = 'ref_uri'
            
            if not location:
                prev_info = (host, uri, ref_host, ref_uri)
            else:
                prev_info = ()
            
            edges.add((host, uri))
            edges.add((ref_host, ref_uri))
            edges.add((ref_uri, uri))
                                    
    print("""
    <!doctype html>
    <html>
    <head>
      <title>Network | Basic usage</title>

      <script type="text/javascript" src="./dist/vis.js"></script>
      <link href="./dist/vis-network.min.css" rel="stylesheet" type="text/css" />

      <style type="text/css">
        #mynetwork {
          width: 1800px;
          height: 800px;
          border: 1px solid lightgray;
        }
      </style>
    </head>
    <body>

    <p>
      Create a simple network with some nodes and edges.
    </p>

    <div id="mynetwork"></div>

    <script type="text/javascript">
      // create an array with nodes
      var nodes = new vis.DataSet([
    """)
            
    for key, value in nodes.items():
        if value == 'host':
            print('{id: "%s", label: "%s", shape: "box", color:"#FB7E81"},'%(key, key))
        elif value == 'ref_host':
            print('{id: "%s", label: "%s", shape: "circle", color:"#FFFF00"},'%(key, key))
        else:
            print('{id: "%s", label: "%s"},'%(key, key)) 
    
    print("""
     ]);

  // create an array with edges
  var edges = new vis.DataSet([
    """)
    
    for start, end in edges:
        print('{from:"%s", to:"%s", arrows:"to"},'%(start, end))
    
    print("""
        ]);

      // create a network
      var container = document.getElementById('mynetwork');
      var data = {
        nodes: nodes,
        edges: edges
      };
      var options = {};
      var network = new vis.Network(container, data, options);
    </script>


    </body>
    </html>
    """)
        
      
        
if __name__ == "__main__":
    main()