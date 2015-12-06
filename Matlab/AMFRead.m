function [v,f,normals, colorTable] = AMFRead(fileName)
    xDoc = xmlread(fileName);
    vertex = xDoc.getElementsByTagName('vertex');
    v = zeros(vertex.getLength,3);
    allTriangles = xDoc.getElementsByTagName('triangle');
    f = zeros(allTriangles.getLength,4);
    
    materials = xDoc.getElementsByTagName('material');
    colorTable = zeros(materials.getLength, 4);
    for i = 0:materials.getLength-1
        thisMaterial = materials.item(i);
        mid = str2double(thisMaterial.getAttribute('id'));
        color = thisMaterial.getElementsByTagName('color').item(0);
        r = color.getElementsByTagName('r').item(0).getFirstChild.getData;
        g = color.getElementsByTagName('g').item(0).getFirstChild.getData;
        b = color.getElementsByTagName('b').item(0).getFirstChild.getData;
        colorTable(mid,:) = [mid, str2double(r), str2double(g), str2double(b)];
    end
        
    for i = 0:vertex.getLength-1
        thisItem = vertex.item(i);
        coordinates = thisItem.getElementsByTagName('coordinates').item(0);
        xValue = coordinates.getElementsByTagName('x').item(0);
        x = str2double(xValue.getFirstChild.getData);
        yValue = coordinates.getElementsByTagName('y').item(0);
        y = str2double(yValue.getFirstChild.getData);
        zValue = coordinates.getElementsByTagName('z').item(0);
        z = str2double(zValue.getFirstChild.getData);
        v(i+1,1:3) = [x, y, z];
    end
    
    tc = 0;
    volumes = xDoc.getElementsByTagName('volume');
    for i = 0:volumes.getLength-1
        thisVolume = volumes.item(i);
        mid = str2double(thisVolume.getAttribute('materialid'));
        triangles = thisVolume.getElementsByTagName('triangle');
        
            for k = 0:triangles.getLength-1
                 thisItem = triangles.item(k);
                 xValue = thisItem.getElementsByTagName('v1').item(0);
                 x = str2double(xValue.getFirstChild.getData);
                 yValue = thisItem.getElementsByTagName('v2').item(0);
                 y = str2double(yValue.getFirstChild.getData);
                 zValue = thisItem.getElementsByTagName('v3').item(0);
                 z = str2double(zValue.getFirstChild.getData);
                 disp([x+1,y+1,z+1]);
                 f(tc+1,1:3) = [x+1, y+1, z+1];
                 f(tc+1,4) = mid;
                 tc = tc + 1;
            end
    end
    TR = triangulation(f(:,1:3),v);
    normals = faceNormal(TR);