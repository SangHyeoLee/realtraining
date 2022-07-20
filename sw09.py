    P, Q, R, S, W =map(imt, input(). split())
    A = W * P
    if R> W:
        B= Q
    else:
        B = Q + S*(W-R)
    print(f'#{test_case}  {min(A,B)}')