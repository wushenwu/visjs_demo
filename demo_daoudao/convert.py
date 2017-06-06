import sys

def main():
    '''
    "027ie.com" [label="027ie.com"]
	"siaoao.com" [label="siaoao.com"]
		"027ie.com" -> "siaoao.com"
    
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
    nodes = set()
    edges = []
    with open(sys.argv[1]) as fr:
        for line in fr:
            if line.find('label') != -1:
                label = line.strip().split()[0]
                if label.replace('.', '').replace('"', '').isdigit():
                    continue
                
                nodes.add(label)
                continue
                
            if line.find('->') != -1:
                start, sep, end = line.strip().split()
                if start.replace('.', '').replace('"', '').isdigit() or end.replace('.', '').replace('"', '').isdigit():
                    continue
                edges.append((start, end))
            
    for label in nodes:
        print('{id: %s, label: %s},'%(label, label))
    
    for start, end in edges:
        print('{from:%s, to:%s},'%(start, end))
        


if __name__ == "__main__":
    main()