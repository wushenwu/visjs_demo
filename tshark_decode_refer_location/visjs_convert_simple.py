import sys

def main():
    '''
    this is the simple version for vis

    host||refer|location
    '''
    nodes = {}
    edges = set()
    prev_info = ()
    with open(sys.argv[1]) as fr:
        for line in fr:
            host, uri, ref, location = line.strip().split('|')
            if not ref and not location:
                continue

            nodes[host] = 'host'
            if ref:
                nodes[ref] = 'ref'
                edges.add((ref, host))
            if location:
                nodes[location] = 'location'
                edges.add((host, location))

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
        elif value == 'ref':
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
