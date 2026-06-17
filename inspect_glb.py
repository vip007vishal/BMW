import json
import struct
import sys

def print_glb_nodes(filepath):
    try:
        with open(filepath, 'rb') as f:
            magic = f.read(4)
            if magic != b'glTF':
                print("Not a GLB file")
                return
            
            version, length = struct.unpack('<II', f.read(8))
            chunk_length, chunk_type = struct.unpack('<II', f.read(8))
            
            if chunk_type != 0x4E4F534A: # 'JSON'
                print("First chunk is not JSON")
                return
                
            json_data = f.read(chunk_length).decode('utf-8')
            gltf = json.loads(json_data)
            
            nodes = gltf.get('nodes', [])
            for i, node in enumerate(nodes):
                name = node.get('name', f'Node_{i}')
                print(f"{i}: {name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_glb_nodes(sys.argv[1])
    else:
        print("Usage: inspect_glb.py <file.glb>")
