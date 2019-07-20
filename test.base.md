<!---------------------------->
<!-- multilangual suffix: en, kr  -->
<!-- no suffix: en -->
<!---------------------------->


<!-- [en] -->
# Easy Dynamixel Helper
<!-- [kr] -->
# 쉬운 다이나믹셀 헬퍼
<!-- [common] -->

![PyPI](https://img.shields.io/pypi/v/dynamixel-helper.svg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/easy-dynamixel-helper.svg)
![CodeFactor](https://www.codefactor.io/repository/github/ryul1206/easy-dynamixel-helper/badge/master)
![GitHub](https://img.shields.io/github/license/ryul1206/easy-dynamixel-helper.svg)

[English](README.md), [한국어](README.kor.md)

<!-- [en] -->
This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.
<!-- [kr] -->
이 헬퍼는 다이나믹셀 SDK를 래핑(wrapping)한 것입니다. 다이나믹셀 SDK를 어떻게 사용하는지 몰라도 쉽게 모터를 설정하고 구동할 수 있도록 만들었습니다.
<!-- [common] -->

<!-- [ignore] -->
<!-- TODO: update figure (direct writing on the control table) -->
<!-- Your code ===> DXL Helper ===> Your motor(control table) -->

<!-- [[ multilangual toc: level=2~3 ]] -->

<!-- [ignore] -->
<!-- README-Template.md -->
<!-- https://gist.github.com/PurpleBooth -->

<!-- [en] -->
## Getting Started

### Prerequisites

You need to install the official [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK) before using this helper.

<!-- [kr] -->
## 시작하기

### 사전에 필요한 것

헬퍼를 설치하기 전에 로보티즈 사에서 제공하는 공식 [다이나믹셀 SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK)가 있어야 합니다.

<!-- [en] -->
<details><summary>Click here: Dynamixel SDK Installation</summary>
<p>
<!-- [kr] -->
<details><summary>클릭하여 보기: 다이나믹셀 SDK 설치 방법</summary>
<p>
<!-- [en] -->

1. Clone the official SDK repository into your custom folder, for example, I created `~/lib`.

    ```bash

    <!-- [kr] -->
    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```

<!-- [kr] -->

1. 라이브러리를 설치할 공간에 공식 SDK 코드를 내려받습니다. 예를 들어, 저는 `~/lib` 폴더를 만들었습니다.

    ```bash

    <!-- [kr] -->
    git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
    ```

<!-- [common] -->
</p>
</details>
