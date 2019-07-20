# 쉬운 다이나믹셀 헬퍼

![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)
![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)
![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)

[English](README.md), [한국어](README.kor.md)

이 헬퍼는 다이나믹셀 SDK를 래핑(wrapping)한 것입니다. 다이나믹셀 SDK를 어떻게 사용하는지 몰라도 쉽게 모터를 설정하고 구동할 수 있도록 만들었습니다.

1. [시작하기](#)
    1. [사전에 필요한 것](#-)

## 시작하기

### 사전에 필요한 것

헬퍼를 설치하기 전에 로보티즈 사에서 제공하는 공식 [다이나믹셀 SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK)가 있어야 합니다.

<details><summary>클릭하여 보기: 다이나믹셀 SDK 설치 방법</summary>
<p>

1. 라이브러리를 설치할 공간에 공식 SDK 코드를 내려받습니다. 예를 들어, 저는 `~/lib` 폴더를 만들었습니다.

    ```bash

    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```

</p>
</details>
