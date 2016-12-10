import sys; sys.dont_write_bytecode = True # avoid .pyc files
import json
import overpy; overpy = overpy.Overpass()

txt = open("nodes.txt", "w")

result = overpy.query("""
<osm-script>
    <query type="way" into="hw">
      <has-kv k="highway"/>
      <has-kv k="highway" modv="not" regv="footway|cycleway|path|service|track"/>
      <bbox-query e="-77.039006" n="-12.064528" s="-12.093128" w="-77.063135"/>
    </query>

    <foreach from="hw" into="w">
      <recurse from="w" type="way-node" into="ns"/>
      <recurse from="ns" type="node-way" into="w2"/>
      <query type="way" into="w2">
        <item set="w2"/>
        <has-kv k="highway"/>
        <has-kv k="highway" modv="not" regv="footway|cycleway|path|service|track"/>
      </query>
      <difference into="wd">
        <item set="w2"/>
        <item set="w"/>
      </difference>
      <recurse from="wd" type="way-node" into="n2"/>
      <recurse from="w"  type="way-node" into="n3"/>
      <query type="node">
        <item set="n2"/>
        <item set="n3"/>
      </query>
      <print/>
    </foreach>
</osm-script>
 """)

txt.write(str(result.nodes))
txt.close()

#print json.dumps(result.nodes, indent=2, default=str)
print len(result.nodes)
