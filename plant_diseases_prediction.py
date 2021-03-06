# -*- coding: utf-8 -*-
"""Plant_Diseases_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14NaMezlSvThw3iKK6cUxN4HAv5QUX1Eb

![image.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANEAAAA0CAYAAAAUs93eAAAgAElEQVR4Ae1dAagkxZluZrrndU82YnZn3nmeF3IhHCGEICZIkCBBRIIECZKIBAkSZDFv+nmet3iyiDyR4HkiIhKCiEgQERXxzE73rCfyEJFFFhEJi3iv++0Z2Vv2lkUWWZZleczx/VVfzd813fPm7b5Vk9uGeVX11///9Vd1/V3//1d1vyC4eF0cgYsjsJURaNUhA7iVH3hofL+s6/z8PLjz4NTxBR0uXeeXdR3ys+r9Or+sedXVEcZ0Fn4djsafNz8vn3nx5m33/wte07hVJh0GowmRA+XX+2Xi2XQ1joM/fj0ORz++/PL913OS3/jvhy+79DdrN/WXDl956d2HLw1WxpquiSfhSHGBhqmmZ76urg5GfJ0KY8q7jem87UMWjavzWs7PM/9lkOHz7O+8bcmN4uC4gjdBNbwpjwaDIFhpJUF+xUKUp0mY74vD/Ggc5uM4ysZ/u7j/LRLf8G9/vnbnncW4nxbj3qA83UvL9/uD9Sd2pcV1wcqhDvG2IbVyCSed16zr4HUw0BDOVMM0T8KJx9THYbmpfh44cZiSJ1PCmQKO/KwyaZlqXMJ0ynqmug55DWceKfMavw42i4emZV7zmJVHHeuZzuLh4/s0FWZEJhLLujOqbqW1EGY/icPRKA7zs3GUjxP7Qx4/q0RCM1GictxP/V9xpDcoH+ylf77c6yBlUO1WZNad93G13Drv82KZOCyT37nAZ9GgDhf5sz0Lnko0ns7X8WD9vHXz4lHGOv6zeBCfqcbVedYz9et0uSkPWtbZrJsrLOuUbWm6WXldV7l5ugL5WT8r4EorDkc/isP8AFYcrThJmKlyZSVq1SlRb4CVSStU8Vlvee3BnctrlzTIYmWQsaCshLGMdF6Yppk37/P2y5vx2Sr+ZvxQv1WeW8WfR4YLhbNVWbeCvxVc3T/Qndt1afDqpXE7ezoJs404zMbVX+6VK0oUUIl6Ys6JSQezTn5QJCgUyjD3+ul62V8qfmL9pnMTdvupOFm3n/MXw/Hz7s/n3d52jer2yd2N9l+VRNlHSZSNE/g8suoYRZIVCKsSVyKkYYMSibJAYSa/vsqb1Ul8p41eWj4S/GJTf2krnSQu07qBnlVXh69hpGWq62blNX5THvTz1NXh1MHq+AFP/7TMmoemrYMTxpR8/DLhmp+f98vz8tC8N+NBnkj58+l9Hu5mkJgImoGrW2iPbkqi4WcSMKAJ5xTJ+D9OscL8TBxmB+P26Om/u2x0u5Wk9ZOHD39j153FI71B8VovLY/aAINaicyq5FYnMfVEmTJr3lFGy9IlWmYCKTtT0rLs0xBO+qa0CU/D58lTHrajaQgjDuuQ+j+No/HmgWucujxhTNk2yrh02c9bFIdTV09YU6rbAE5TmXCm5McyU/Lwy8RnfV3Zp5nqmCb2kVtJO7slCbOz4vtQgVQQwcCzjW6UvZG0s19eEuzfiYgdGNlrWqiV1RCh7t5S+Ug/LUShjBknSmNNOpp2xbi/XLxd4yeBPXnrPGFMWceUcKR1MNbPqiPOvKnmJY0q2eflMQvP5z8L9y+5Tvfzi+wH7+Hmabe978Ykys8YM61quiGEDXgc5hlMPU9xNmduMfpLh3b0BuXd/eXiuJh18I8k2KAVqhj30uKNb9x+OJ6b8ZcbERPg4vXXPgKdTv6dJMo+lXC1URYXOLCr0gmsUueqPP74IbzdT4tX6B8ZhTKKhGAEyovp+lNfsmCD342L5YsjICPQCoLVOImyD+jncA9IonFYgaLsgzgefnPbx2tl3FpM1/f002IDSmP8JlmFxn1E7hCASMtfbtLuPE/5eXB0M8RnquvOJ7/d/HxZLiT/v1TeGKMLJjsYy6/bGf6W+z/VVBTogPF75H6RhjfPL/tw1OPSKfO2KmhBUfppcdb4SXYfySrVYrp2wm7KOnzKrVK/jmWkWkad9+tc+ZJ//mTnzuX1G/pLxbc8evLVffDzukyemk7LwDxpdHlWXvOdhafrSKNhft7H8csa36/zyxp33rzjsSN4fVE2983DG/SuTt0Tn+88OKTxcf0y8aRtXZjKLyxk/yh+kD11ACXiStSNskNfDfb1ZghNfrMEII6fVmgW07UlsxqpzVjZR8KKVD5rZajQKLl8uF/2224sL/5m/Xv9tDhmV8azvcHaHTPaaeSjaP5CcFZ3dKPR7iTKHw+C1fCLlD+J8h8mUXbCPtDPJJ3851+kPJhMM66VVhKNXqTZptNulJ2En1RL/ItDncWl4pr+oLhr12D9iV5aPtdbKl/tLa+P+mn5+jy/3nLxdIX3yrjVXy6e1qFwF/5Oi7OY3AofE/N8rkb6flr8Aaaka3tQHg5WZFKdT3ugZZtMm/ixnmkT3nnCV1qwMPC0T9rZ73AG0u77ncEm+3kwn0NuRHP5m24pCfPXEMiS+Qj/PMr+tF2+uLoP0w0byBzyT0hbnc7r306i7CyElRVINk1xtCcbd6PszgnqxCSCibOYFoe0/+I2TGGCcSNVTiLQv5n4O2KyialWfmj5U+gWwtr9tFhjYEHacHzK53x8lnf+5vAPYRL2BsWt/cH6LUh3peu39ZeL2/uD8tf9peL2/vL6z/uD9Wv7S4cvmxWswKpHGSHH4qD8eBMlovxquCTbBEelrpuVZx1S5nU7PlyXmScdU6FHkCgO89PmaW8irxJ9jfLj8JFtI+TBNnW5Ke/j6nYlH0fZ7UmYffiVILuMyLp/SZi/OpmPvhKtmG2YdvZL2Y5p5z9P+OuMbo3b+a/wVoHh91IH2zBJe3Srw+1kt8Tt0W3d4D95bpPy1aWEKTGr2RaWbhFWHSQ1g5q/52k+mMlPImqV82/K/PLgJnTdWA8l0kIK/166fpNMYo/X4qA88zd3Fou2C04e8NiVFvf20vITo3ST9nqDcqOflgd7g/JgPy2OGL5Q7PWyn5YPi0J5MvSX/utK+GFyxm9QbCymJR4mlJPtQgwNY1nDdF7XE06YTpkHzlZ+W6bDRJNN9TA/Yu+5mPFYkYLgJZ6ypwyav86zL8SblVo6WD/ZWwhi4W2Aun4m4fAabPaLXGG+kXQyBJdsWzjLmb+JQ9BabuThhnTD/CTOeqIxPAywihHP4MgJnKNmm2ZqjK2M03C/YxZxNU44gJVN1Wy80M5+qjpHxkEvLX8gkTSzOpzsDWRiHuml5VlzsLQ4aScrJuyR/nJ5fHLgtPi0Upeur4KxvSYyrozDfloc4ISf0Jfj/tJ6quTSNC0cFzJ0EyXqD8rTl+/+n66sPKgfrN/SHxSnrKxjyAez1JcByiWr2tLhK+2qNWlra5N7Mzo0DRymm+Fve30cZc9WJlmYH7mQPlG3nf00ibKNWUqEMYGCJe3hrZ3O8Lv2ga76vtKyWzIfadnNEbXhNVX81TCJ8icFr5MdTdqjm+1DQvGbUhq/zt4iL4G2SqO0PW2aRNmHdhA9igBK9Dyc7sXl8mZsmoqZs7Ia9tLyY1kFBsVuwpDuSouf8cwczCtdJ/mpFgzARusq5+2sj/LmbFOsGLE9g18YJVLtLKYFQuqO9+Kg+Li/9L87FMok+4tDna/dVcI02ORajWEedDqj730lyq6M49E3lEm0GW1o8DUanPz9V8npeeFVORGiEb38Sgv+DIJFoMdEM4GhZvq4PXpKzHkx6eUpTSWSd8dMP2De1f24YoF/XT1gpg6mG95Bg69tJns2NtsmpGuS8aWOXbHQV05u6Tf6mETZGfKz8/mJ6qC81EmifBUrW6fzH/U+viGo8K7yaCh1w/zBii8kJh2cudH9dSQwpfpp8SlWI12PCdhPS6xAcMaxgrlr11K5JP7SoBjLy3iuZnYGCgqeE4UwvlY/LU6pc3VTTPoDrURCQyXCAMm1c3ntCiqRjcAh+ncj66GkCHH3But39PEiYVp8Zs0+h2IyqyGeqgth9koSZkfjENGk7BRupHGI8yNxOHxAmUYgs3LIxNqBJy1eMUmi7LRVvB1JmD8ah/kJczpEfJWNbpi/3u2+Bhu+9sIki8P8t0mYfxCH2ck4zI+bJ7ScMDmDSQTlriFuQYlUWzhs7JQoDrNr4zA71viLshdNn17qxGH2iY8HXni4xO18Tcwve1CZ7WHMhCbKjlnzyoq40oLyL0SjpTjMPkSkLghyvi5T6UYSjR7jmIMvfPxu9MeriBSHw71SH2U818kqpm5uTO4PqzZJcfaNoWymGHg12BXmi+Kor+1VDUm9nZQbmJi7ltevVvVBb6l4lKbT1+4svqtEIu/GtJeWr4JWRcnMBuxSCXuXdGDp8r1Bgeig3aiVdEqJ8FatUVCDB/670nIJ/egNygd6S+Ub/bQ8JZu94pcVZ5UvJu0hqtXtZK/bJ9846WSPYPWWV0ei7E8YT/PuVTbGHtyk36vhQpTdCcVbCPNPMd7mQZadlSBPmL+XGAX42CiBeX/L3J/sQJ2ZBX8hCa3/0MmOLiy89i08/eMo/7WRj1sW2XHryHO8kIoSmTeT3cFip0QSvZPDyPl7Iqs+QxlmD3ejDA9UibTF4f7rkzC7B5MYuHhIL4T5DUGwrxt3RrfFUfYc30eT/pgg1p5ulN0RR9kd2BfCymQe7vlbcWhWGDs3TwXBKq0FkduOKVbASxMosJYtMmNlrS08RF6wJh7ni8fDzSEN17iCwEqbinPmHMrJDcsYmSE+739LzKjqdxKAE/SXyh9BgfqDYsOaPqRt9QfFi1KHekTFzMV6lOryAusNynvcSuGCDHKCgY4+aV2Klci1Z2SaUiKcxxMlMX4dT0kgqndtbyArj31xkBHF8pR8I8Ip67iVdLJ9kzHLz+q9tDjMH2SdnTQnJpN/NYZTnIT5KeKIbwBbPcxejcPRfWblWg27HfAR88q++CirynXqoYHAEPZTnIO9IHs8HNPVHUmU0znny5N3qzGXcZOVSE9AtRIRF2aqtON8Z0RvcX6SbTEdt5L2cC3p5PuqfknQwsPD9RntTQcWAvjiWE2p/LKymDb9eenuOWSQyBvHSvBl3O5NouxwEg3X8DBQstpp6JIKL4Wn4Q7ZZcA0CfPT9ilozQ+EEkfvOKQ5MzB7JBScFmcqvsXKuNUblO/aSX1KfKg5eQLtu//639d881/W3/V/375Xggu1nMSckwOtJrTeG0z7RDhNDpkYRl9MizNYhYShkfkFRhUFJy1Oatll7KLstDUdsIfxkXrKBdgaMDffmHVJlG/YcKqVWVaJX4nJRz80zDaSKH9e87HtyMuQmFTGRKya2gsdmH5iwsi2hI1i2Xag7Pj+BWmzcdzOf+8PHH0i4mlzboIrvOyDw/CDkk/qTW5hYf+3oGw2MFWpNko0kUXGyETnKngYg7gzzCZ9Fppjnlk8RQPLgH1QY3IGkT4PeXuKsL9xc6Ux+56QaRjL3tauflo8CZOon5bHKk7/yqFOb1AeNX5NeezzOJFtfCKagBI84EpkOgUlScvnuJkqCn7X2sO6xwh92/7QlKwoEW6mvKxoJ2/cyR7S9GKeVMd0Iw4QaJALT7cAK4iYUO4drWzcbec/szg2WQ3jKD9u7hEmUj6lBLLfIgome3vHYRJpHnEIv8zQ4smPt5R1PfJaibBSgKYusBSH+XVcIcwKm30MU03zSzrZw0kEOAMOUit9hhIZWezqivGbViLBhbJXNlvDTIfddZMub6N1sjCwHbgsQSBfmXJ425aRoz5mJ9htsorQNU8q2yiXNhSloxSml5YH7aT8gDCkcM4X0/KMPPUH62VFwTSiyZMn02mMOSBUIpFHzDkb4g6CAErcS4tHnM+Ulhu9tHjUjxLK/hFPLJhVzVOiIIBvgU0988TlEZmVFmz6xOz+G3PFmElaiaQXYoaJEtJ3yrmtoHq5GiZi5tnvWtQqgZjl18H/qR4QXt2BT5gl1u8SBRL6EZXI3c+JEk37REoY7LkgVPy+VTS78iFczMtsmXTNQ8XxZ61RIttfmFwTc44oLo3b2e9NO/bhMa1EtfPEKjH3uyAjFoprHeP5MrW8Seo6Zs7LmVMKsmzKSe18jAmglMThWxiZO/hXd3/UgzlkggdlpvBaCCQYU07eF3pf13l5Xz7h//3v7+teccXotiuu+M/K7x/+/nUMipPB5oWH8Ykm+0S9QXl212D9IQnND4rjVp7PemkJk806xVVeokTOBxNeVCL2n/LKZh4UqdvOn0nCHNEp+DYH5YGEFcKMK5WIMosvY3AwcYGXjxHpU/2CwxzGneyo5WEedmYlcXx033FP4VPFYf52Eman4zBfNb6XPY2CVaY9pUQmOoc6yjtZidhf154frDBPehmOVtIZ3iym3MJ+fWjX0YoScZ5VfSIwcHjIYyUSJRJ8Mee4ElXwPLrAmMDDzzCek3HLPrDbDTNpPV4+blVAIBvb1T7hlFPZjfI/WGa6YzpfYS5HasRBh6KsP6UFQdiYStQflPC1SCujrsqEV1I8WbksV9Ioe76JdkqJsJIsFx/00/IVRN52Lq3fUPPGbKXdTZTI4u7rJmG+B6aPMXHER7oH5g3MOUwA9atVIlUvuNaPULJgJcqPOjxYDhMlsvdkpYUIWRzCH8AOvoTE3/lKZ/Q9+BZuM91OXkXv2pkRWHA4k/He15XV0fXPRBVRD4XqdvLXrfk0RWt8IjUuk5VoCpcrEfuOh5M1EadwJ7IFLfM2An1EtiVjco/Gs/nGed2Ay3lrUpgjOLnNp49MUnNe7o0q5owSDoymBY7UjOH3LKbFvRpbAg4Ts8h91FFwVsatzXwkE550IWAbCsbAZN5m2qRVhLiNPPSLJubcBGt2jj6R4sOVSAitw4+9HStTNk46o1vJ1fhEZnXBuIrvOfGJBM34RGal4thPO+PGnDP1xgzyfRrrE5n7aHy0g0HwEkPBgfhEIqcZR7USUdyKTyTzYbISORydYdTQ9A39Gz1mLZsNe9pao7u884lklbAfuZn2iQT/XHwi67Od7UbZsxJkYL+xykfZSXuezsmzDRnZxT0hdqmbDDJBP1ZOJbSeF58AKAt8MV27TfwdE0oeLy6Vyj4Ogl1peZ+rT4sDpEMqG7fL5duWOduppOaJLk8R81QXO9o9VZwcim8w8YmmonPkzf40pmYlsgdpTRSvokRQYvvEF7s+jvKDOqomcjtZ5WnIlci16XwiTHyLq8w5i2dXItTbJ79Wojh44+tmc1fum/goajUDj8lKZNvQ9HbcrDlnx9nIowMLGDc9di3zAGZ0UtrGPHrcRPUqgQbSCr2sRK6/tUrk2nHmnOBXzDmOIXlLGVsM2CtCwAd7dfZg9RnObxMtHb7ctEpapmxfp8yz3epgxFH2Lm+OMUlkQM7aIygVIVUjAsfpA9nJtysNfKJd6eFvKzzZaJXTCrJhisDC5HUCawZCsXCxLZ0GcZQ/UyPfGEf3FV2FXsw5OUlu/SKenatOhAqNN0kCUSJ5qxabsXIKg0oE+QLsvhu5rK/RzmHG4pJ6CXFXbPKcSiT1wBMlciaRURKrRJYVEppzph20qcwxrCC3mfvm6hlKt+NoVrLJGFZ8IrYzUSLKM1mJKC/7ZvmK6abO25n2F2TDufZeCh/tT4lMUOyGA6hGicDX8Fbm3JQs1mx9Dcd/Jpu/MO2yh6rjk3HusB9uDLw5WAef6pgg4VBedZfXPNHiaLS7hqlpGOfhBusPmbdQMVGxISk7/8eVeSa4veXycRtwkI3YxbvkoCded/gOzt/B2VfteIOzGponi5lgMoHMTd6wYVwORCV1JxZsYADfAJcDqFVFZVt6sJg3StQcWIDTe1hPTBzbn/RDwt8Hq+OajbFZOcGxIW5n1piomFqJbJ+oRGoMJj5RK45Gt3OSGXmq7SSd0c0VOTF+Yf6ylYNj4AILDreqRJXxZR9wqkUOkVLxomwDJp3Pm/hI43B4vWtD6CCve1+t0s5WfKIkGt4t4xAO91RXGmw2Z2W1zeGaPflQaU/L2ZB386OSwb6EacDY9sYeFlt+tSm23kvXfiwmmnlCiy9kfaLXKsyDoNUfrO+lv2RWpOJ0b1Cu4WQ1eCym5ZJH44oIS7qnCJZ0+0RKovwDbTo5AhvC7qfln8y+lKwgUPKzvUGJmzvfJZutxdOGh/H1+mlx2m3Gmj2eF8xNs3JJJGz/9XiqIjATd7IR653fgNMI8o6LOWS5sDC8SeqsuQJ8PKlV3+QgaTfCsX6aWjmepK8Sx+6L2L0+yjJ8GeZWtz26ETv1STh6h/fVjuEpsx9Fs2s1XAjzV10bZpxPwO+bPWBjvM7wpuL9JuVqptvXTaLM7HtJO5h3OFu4r4v7jWCXocU334cvy5jYjWKMgz4VYvDwXZAcCiQBFX+PDDhYjdg3SU27z/v7W1ZmKpYtbp60ApxawLEQ7B/YDTnb0IZ9ck5xkRfb5CltfQ6b7y+t4/VdfbVwjm7iExnzCkplVqfipHceTdHybVtfrnzc7eQ8h4YOu6s3KB/rpeWaUXBrhtnVZDEtT/TSMrt890d4zb3x6g3WrrInLPAOkpy/w8kFe2rhGDaVQdzp7MOLjOqAqF0pwmyjG2ZvJNH+qzG5JuNq8jgrJ+fDwjxLwuyUGXP7ADN+z+kY3/LDf9wwh1ARMrdn8GxgIYRJkr/fbQ9vwqRNouHveDpCpRs40NpdGN6UhNkrnOj23o4NXn4v9pHAy0zWCX/LB21XNpHtE9qNH/wvo5gIrMj7PqzTk1HfJ3s8Bx/7tPtEMvfyE1ASE6LPrl2Q84POjDObzAb/yEKYP4J+x1H+gvWBJvXt/LA5q2fESMLsCbx0aDa1Oc72gRRlH8dhjnOg533BJHgRq5E0ZM0LY4rgdO700XT7mauTmGSiEIMSUbk3a/9VCqJ3/1Q8ywmpDnTic8H+F3w42C28P4Kni4n1G1PH7JDnXP4drh2BFlY1hLD7y+t7zQt6xR6ku5bK+/qDtb34aD42f9WIkQdBxszEnpLwKe4HXX95bW9/UNwP2K6lwr3LJOH3dv6UPZ2Mfy1zAMf8EYaFoiRR/l4cZm8shKPHYB4vyMqw/2qcRI7D/AHcwCTM7+XP7u/sjTv5g6Jo0Wg3TtMDbnCGe5BavAfsBqLZS4pGt8chDmzmR+J2Xnaj7A80k0wYHgdicfhzdB/eAIXy4BgS/AfzpIY8aCvfG4cZ2rwfcpiV0fh5ngJh7Fr25MaHyeRNWI6prZehZZ5pAFNwIcwfx/cLsQrKgVN53SMIcB4PZw/NGFlZRLZMZMI3IESJRFaO4XCPGZfR/Um0jweg5axe8xiij6PblOkGYSkjUzc36iqBJHDZ1TZLuIsAMaLh7fSSsawwOGHdS9dXMTntuTLWC18nEN41GhS7e4My66flW/3B2jPeSW+PDgcvcTraKLaYm+YpDfnesopNmqbU9K76F7j6Ii1gdXnC/JQ8AOf7NqEnl4VPPYR8XroMZrqs86apaj3xbR3a4k/zcTDia75NebbXRCNwG+rHSfTHZ8je1EYdvK69OlgdLWHz4ANHX6SdlWp8P4+jHNm7VdPC7HEgXIhj5j7FhSybyJZpXy/DMBum91EupCQXeW82Agn+yVuUbXQ6r+tXXDYj++ushx2pAwy0rY0NPXzR7htBS8/laqKbgpuwb3aK7TM1cuB0uXuyT9FuIlgdfh3MZzMPDmia8DRc5/12trvc1FYTXLc/D449R4eX5fK3m4JQmmlNvqmdJngNiylQE20THAya6gBvqptq2Pz7yDB/zSiSdfgmoctxEg2fVOaKbthvhGUtgJ+nAMQVfjbSdMzJwPCvCYXifZkfqk6RJ3kw1bKxHaYax8fTdcjrXxM94Zvx8vE2401ZiEf+88JJNw/+OfM2Pp5YDL+yHWS7W+GpcUk/j9zngkP+us2t5IErVx0jgSEihIiTceYxODY6YuP53Wj4jDrervmAMcpMWTd3alegYybSw70qZ1Lat0Ydf78dlgVByUK4L5vG82XUND4dcUmvU9bpVNczr+uR5+Xn6/B8mC5rPhru54EHGFO/nnW6Xucdvg3jH7evbNfieA8jR6vgpGO6Gc4svLllV+3r9jblrZEb8/YULsKjel/GBhwkTPu2d5rB51UnSBNMTALrA03e8nQroNtgPKBi+mivjp8vB8tNuE1w0p1vWse/DrbVdjQPnW/io3F0vgmf8Jm4Xw1We/LSXJjvmUMpyVOnM/k3THJNv135rcgB3HmuccsdLmS4G/sUshHI1Sn7FO/Rq4k9D2MPZ6WFMKfZU7Hxe7viSYDDtievFsTyET6P/mLx4gh8eUYAGo1LpYjWDZ+kacWonfNV3OkBbFaN7usG+ALNTIefvGXlwccs5Os4UX7WhNLNisN9IAU7tkO+N6Zls9JW5K3Ir/syK+8YbZJRsjs56kg0nq5vggNH183Ksw4p834bGq7xmGc9U9Lrer/Ox6krkx51Ou/jat5NefLwaVmep564lEW3RXpdp/Os91OfR+UmsJKMFPEK3s1/FIpkfKM6887t0uMTxO/EYfaw+VjE/qtxfAObkdg0FaWJ8tRs9mVHqZwSefP3p2jKhdkn5oN9FXkhHy8tO2Dsg04JZ0oazcPH13WkY0rcpjLhSHHp9khLWF3Zp2G5DtfnU4er6fw88Hn5dXW8gVuHR9gsXrNwNuNLWqT60nDWMQVeUz1xWE+eLDOtg9cyZWNMyQCpROy60XAJb0i6VYiT3KYShMCxDVUGrqwq8t/GnV8z2cj1cS0+eSRRdmDyHWURRMtlZZvqj4+j8cDErydMGvAmvIZpPpoH6TXMz2ucJp4arvM+rwtR1vL5/GfV+bh15a3QX+h++7L45Tr562CUc+spImfdMD8kq5I15cy+jfFl5HwYVhTWYfWSPJTJRNh4dgs4BmZTliXN8VnZR87P19p6/77EFLiRF6/pEeAEn645f8iWeW/hJuWXdM3XNe3XPc0LVWbFscoiKxKUw5TNilQ9RGiUiPhUJNmXOoi3WJVvNc9wNMm/VXhTW018mvDnhV8ovvO2T7xzkWNeGuARlyna1epYEPMAAAHnSURBVPm6MmWblfo8NO6sOo23rXk0yt+mjOV0cSQHB086s41RPKbWvDP7TfbwKOv8FJ/PlY+L82s5IkLdQPgwlnVal9d9Yj1hTWXCZ6Wsq+OFOv50PWE6RT3KTanG1Xh+XuORl49jWpn89Wk0HWkJ0ynzxNHprDzqWE8eSHH5cF1mPWFI/V8TjoaTRsOa8hqXOFONAomVJNCprjOYFcHzS/C5KPwjJvdJJvF1zErkggfW/2HELQ7xnbv8EI75m08VS1SP7eo2fVhdHXHqUsqsU+Dpi3SA1eUJ81PyABwX6/08y4Jk/xC3LiV+U51fz7Jl7eSoowcMV1OdD7fojTRb4eXznlWu41sH2yoPH186pv749XVlhb6tWSgB/ntB9gMcm0eELm7nz+D1ioUwf1ne+Whnv8MRfnn3RF4Fnrwivq2iXGR2cQS+4BGA5vmXD/PLPn5TuYluq3DNv4lW4+h8HX4dTNMgPw/OLDxNr/N+O9tdbmqrCa7bnwdH459rvqmdJvg87TTRNsHBs6kO8Ka6WlmakDVcMyWcKZmy7ONquI+rO0I6pnV1hNXhsA6pf1EGwnXZz5O3DyetnzbhaThoNF9dV5cnrqabJ0868mS5jrYONouOvGbhbIWnxt1u3r6M5K/bnDv/f2+hj8zlpaXVAAAAAElFTkSuQmCC)

In this project we will create a Convolutional Neural Network which will be able to predict whether a plant is suffering from a disease. We will use different layers and other hyperparameters for building, training and testing this classifictaion model.We will be using tensorflow and keras for this project.
"""

# Load the Drive helper and mount
from google.colab import drive

# This will prompt for authorization.
drive.mount('/content/drive')

"""First we will mount our google drive on colab so that we can use the dataset directly from our drive. For this you first need to upload the data on your drive and then mount the drive on colab."""

# After executing the cell above, Drive
# files will be present in "/content/drive/My Drive".
!ls "/content/drive/My Drive"



"""After mounting our drive we will locate the folder where our data is stored to use it in our colab notebook.
Here you can see that I have 2 folders in my drive and 'Plant_images_pianlytix'  contains the images that we will work on.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
import cv2
import random
import os
from os import listdir
from PIL import Image
from sklearn.preprocessing import label_binarize,  LabelBinarizer
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, array_to_img
from keras.optimizers import adam_v2
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dropout, Dense
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
from tensorflow.keras.utils import to_categorical

"""Next we will import all the required libraries. As we are making a CNN model we will import all the required layers, activations, optimizers, etc.  """

# Plotting 12 images to check dataset
plt.figure(figsize=(12,12))
path = "/content/drive/My Drive/Plant_images_pianalytix/Potato___Early_blight"
for i in range(1,17):
    plt.subplot(4,4,i)
    plt.tight_layout()
    rand_img = imread(path +'/'+ random.choice(sorted(os.listdir(path))))
    plt.imshow(rand_img)
    plt.xlabel(rand_img.shape[1], fontsize = 10)#width of image
    plt.ylabel(rand_img.shape[0], fontsize = 10)#height of image

"""Now we will observe some of the iamges that are their in our dataset. We will plot 12 images here using the matplotlib library."""

#Converting Images to array 
def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, (256,256))  
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

"""After visualizing the images let us move forward and create a function which will convert the images into a numpy array. It is required because we will normalize our dataset after this."""

dir = "/content/drive/My Drive/Plant_images_pianalytix"
root_dir = listdir(dir)
image_list, label_list = [], []
all_labels = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']
binary_labels = [0,1,2]
temp = -1

# Reading and converting image to numpy array
for directory in root_dir:
  plant_image_list = listdir(f"{dir}/{directory}")
  temp += 1
  for files in plant_image_list:
    image_path = f"{dir}/{directory}/{files}"
    image_list.append(convert_image_to_array(image_path))
    label_list.append(binary_labels[temp])

"""Now we will convert all the images into numpy array."""

# Visualize the number of classes count
label_counts = pd.DataFrame(label_list).value_counts()
label_counts.head()

"""We will also observe the number of images under different classes to see if the dataset is balanced or not"""

image_list[0].shape

"""Next we will observe the shape of the image."""

label_list = np.array(label_list)
label_list.shape

"""Checking the total number of the images which is the length of the labels list."""

x_train, x_test, y_train, y_test = train_test_split(image_list, label_list, test_size=0.2, random_state = 10)

"""Next we will use sklearn train_test_split to split the dataset into testing and training data. Here I have taken test size as 0.2 so my data will be divided into 80% training and 20% testing data."""

x_train = np.array(x_train, dtype=np.float16) / 225.0
x_test = np.array(x_test, dtype=np.float16) / 225.0
x_train = x_train.reshape( -1, 256,256,3)
x_test = x_test.reshape( -1, 256,256,3)

"""Now we will normalize the dataset of our images. As pixel values ranges from 0 to 255 so we will divide each image pixel with 255 to normalize the dataset."""

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(Conv2D(32, (3, 3), padding="same",input_shape=(256,256,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(3, 3)))
model.add(Conv2D(16, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(8, activation="relu"))
model.add(Dense(3, activation="softmax"))
model.summary()

"""Next we will create a network architecture for the model. We have used different types of layers according to their features namely Conv_2d (It is used to create a convolutional kernel that is convolved with the input layer to produce the output tensor), max_pooling2d (It is a downsampling technique which takes out the maximum value over the window defined by poolsize), flatten (It flattens the input and creates a 1D output), Dense (Dense layer produce the output as the dot product of input and kernel).

"""

import tensorflow

model.compile(loss = 'categorical_crossentropy', optimizer = tensorflow.keras.optimizers.Adam(0.0001),metrics=['accuracy'])

"""While compiling the model we need to set the type of loss which will be Binary Crossentropy for our model alongwith this we also need to set the optimizer and the metrics respectively."""

# Splitting the training data set into training and validation data sets
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size = 0.2)

"""Next we will split the dataset into validation and training data."""

# Training the model
epochs = 50
batch_size = 128
history = model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, 
                    validation_data = (x_val, y_val))

"""Fitting the model with the data and finding out the accuracy at each epoch to see how our model is learning. Now we will train our model on 10 epochs and a batch size of 128. You can try using more number of epochs to increase accuracy but here we can see that the model has already raeched a very high accuracy so we don't need to run it for more. During each epochs we can see how the model is performing by viewing the training and validation accuracy."""

model.save("/content/drive/My Drive/plant_disease.h5")
# serialize model to json
json_model = model.to_json()
#save the model architecture to JSON file
with open('/content/drive/My Drive/plant_model.json', 'w') as json_file:
    json_file.write(json_model)
#saving the weights of the model
model.save_weights('/content/drive/My Drive/plant_model_weights.h5')

"""Saving the model using different techniques."""

#Plot the training history
plt.figure(figsize=(12, 5))
plt.plot(history.history['accuracy'], color='r')
plt.plot(history.history['val_accuracy'], color='b')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['train', 'val'])

plt.show()

"""Next we will plot the accuracy of the model for the trainig history."""

print("[INFO] Calculating model accuracy")
scores = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {scores[1]*100}")

"""Evaluating the model to know the accuracy of the model.

"""

y_pred = model.predict(x_test)

"""Next we will use our model to predict predicting the testing dataset label."""

# Plotting image to compare
img = array_to_img(x_test[10])
img

# Finding max value from predition list and comaparing original value vs predicted
print("Originally : ",all_labels[np.argmax(y_test[10])])
print("Predicted : ",all_labels[np.argmax(y_pred[10])])

"""Printing out the original and the predicted label.

## Conclusion

We started with loading the dataset into google colab using google drive and visualizing the images. Normalizing is an important step when working with any type of dataset. After that we created a CNN Model which is further used for predicting the plant diseases using the image supplied to model.
This model is highly beneficial as it can be used by different agricultural firms and farmers to increase their yield and stop wastage of crops due to disease.
"""

