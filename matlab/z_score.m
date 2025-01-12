%%
%{
Z-Score Normalization - method1:
    1. For each trial do:
        1.1. Calculate [?i,STDi] over baseline frames (2-27) per pixel i.
        1.2. For every frame in trial:
            1.2.1. Normalize pixel i by [?i,STDi]
%}

%%
%{
Z-Score Normalization - method2:
    1. For each trial do:
        1.1. Calculate [?i,STDi] over all frames (2-180) per pixel i
        1.2. For all frames do:
            1.2.1. Normalize frame pixels by [?i,STDi]
%}

%%
%{
Z-Score Normalization - method3:
    1. Calculate [?i,STDi] over trials (pixel wise), dim = [1000x256]
    2. For each trail do:
        2.1. For each frame do:
            2.1.1. Normalize frame pixel by [?i,STDi]


%}