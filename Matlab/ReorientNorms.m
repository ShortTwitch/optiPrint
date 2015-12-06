function [norms] = ReorientNorms(norms, flips)
 if flips(1) > 0
        for i = 1:length(norms) %rotate around x
            ynorms = norms(i,2);
            znorms = norms(i,3);
            norms(i,2) = ynorms*cos((pi/180)*flips(1)) - znorms*sin((pi/180)*flips(1));
            norms(i,3) = ynorms*sin((pi/180)*flips(1)) + znorms*cos((pi/180)*flips(1));
        end
    end;
    if flips(2) > 0 %rotate around y
        for i = 1:length(norms)
            xnorms = norms(i,1);
            znorms = norms(i,3);
            norms(i,1) = xnorms*cos((pi/180)*flips(2)) - znorms*sin((pi/180)*flips(2));
            norms(i,3) = xnorms*sin((pi/180)*flips(2)) + znorms*cos((pi/180)*flips(2));
        end
    end;
if flips(3) > 0 %rotate around z
        for i = 1:length(norms)
            xnorms = norms(i,1);
            ynorms = norms(i,2);
            norms(i,1) = xnorms*cos((pi/180)*flips(3)) - ynorms*sin((pi/180)*flips(3));
            norms(i,2) = xnorms*sin((pi/180)*flips(3)) + ynorms*cos((pi/180)*flips(3));
        end
end;
end
