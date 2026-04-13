# ジャイロスコープと加速度センサー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/gyro-and-accelerometer

# ジャイロスコープと加速度センサー

デバイスに内蔵のジャイロスコープと加速度センサーにより、物理世界におけるデバイスの動きに関するデータを取得できます。

![ジャイロスコープのスケッチ。動きを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる紫色になっています](https://docs-assets.developer.apple.com/published/26996f2ad3b4ea29f84b4581d3bcd3aa/inputs-gyroscope-intro%402x.png)

加速度センサーとジャイロスコープのデータを利用すれば、iOS、iPadOS、watchOSで動作するアプリやゲームでリアルタイムのモーション情報に基づくアプリ体験を提供できます。tvOSのアプリでは、Siri Remoteからのジャイロスコープデータを利用できます。デベロッパ向けのガイダンスは、[Core Motion](/documentation/CoreMotion)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Best-practices)

**モーションデータは、ユーザに具体的なメリットをもたらす目的でのみ使用する。** 例えば、フィットネスのアプリであれば、このデータを利用してユーザのアクティビティや一般的な健康状態に関するフィードバックを返したり、ゲームであればゲームプレイの品質向上に役立てられる可能性があります。データ取得のみを目的としてデータを収集することは避けるようにしてください。

重要

アプリの目的を達成するためにデバイスからのモーションデータが必要な場合は、その理由を説明する文言を提供してください。アプリやゲームが初めてこのようなデータにアクセスする際に、この文言を含める形でシステムが許可を求める画面を表示します。ユーザはそこでアクセスを許可または拒否できます。

**動きのあるゲームプレイ以外で、加速度センサーやジャイロスコープを使ってインターフェイスを直接操作できるようにしない。** モーション情報が関係するジェスチャは、正確に再現するのが難しく、ユーザによっては身体的な理由で困難な場合があります。また、バッテリーの消耗にも影響を及ぼす可能性があります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Related)

[フィードバック](/jp/design/human-interface-guidelines/feedback)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Developer-documentation)

[処理されたデバイスのモーション情報を取得する](/documentation/CoreMotion/getting-processed-device-motion-data) — Core Motion

#### [ビデオ](/jp/design/human-interface-guidelines/gyro-and-accelerometer#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10287)
