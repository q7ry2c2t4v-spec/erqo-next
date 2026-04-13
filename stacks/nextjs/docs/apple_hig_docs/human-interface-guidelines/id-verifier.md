# ID確認

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/id-verifier

# ID確認

ID確認を使用すると、外部ハードウェアを使用せずに、iPhoneアプリを使用して対面でモバイルIDを読み取ることができます。

![IDカードの下隅から始まり、徐々に大きくなる曲線のスケッチ。ID確認を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/8d77246d289837a097f0556d6e7d2c7d/technologies-ID-Verifier-Apps-intro%402x.png)

iOS 17以降では、アプリにID確認を組み込むことができます。これを使うと、iPhoneでISO18013-5に準拠したモバイルIDを読み取り、対面でのID確認に対応できます。例えば、コンサート会場の係員はiPhoneアプリを使用してユーザの年齢を確認できます。

ID確認を使用することは、ユーザと組織の両方のメリットとなります。

  * ユーザは、年齢や身元の証明に必要な最低限のデータのみ提示します。IDカードを渡したり、デバイスを見せたりする必要はありません。

  * Appleは、証明書の発行、管理、確認プロセスに使用する主要なコンポーネントを提供することで、アプリ開発を簡単にし、信頼性の高い一貫したID確認を実現します。

アプリのニーズにより、ID確認を使用して以下の種類のリクエストを行うことができます:

  * **提示のみのリクエスト。** リクエスト元のiPhoneのシステムが提供するUIに、個人の名前や年齢と肖像写真などのデータを表示するには、提示のみのリクエストを使用します。こうすることで、リクエスト元が視覚的に身元情報を確認できます。提示のみのリクエストを行うと、ユーザのデータはシステムが提供するUIに表示され、アプリに転送されることはありません。デベロッパ向けのガイダンスは、[`MobileDriversLicenseDisplayRequest`](/documentation/ProximityReader/MobileDriversLicenseDisplayRequest)を参照してください。

  * **データ転送リクエスト。** このリクエストは、法的な確認要件があり、個人の住所や生年月日などの情報を保存/処理する必要がある場合にのみ使用します。データ転送リクエストを行うには、追加のエンタイトルメントをリクエストする必要があります。詳しくは、[ID確認を使ってみる](https://developer.apple.com/wallet/id-verifier/)を参照してください。デベロッパ向けのガイダンスは、[`MobileDriversLicenseDataRequest`](/documentation/ProximityReader/MobileDriversLicenseDataRequest)および[`MobileDriversLicenseRawDataRequest`](/documentation/ProximityReader/MobileDriversLicenseRawDataRequest)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/id-verifier#Best-practices)

**必要なデータ以外は求めない。** 現在の確認を完了するのに必要のないデータまで求めると、ユーザの信頼を失う可能性があります。例えば、ユーザが最低年齢を満たしていることを確認する必要がある場合は、最低年齢を指定するリクエストを使用し、ユーザの現在の年齢や生年月日はリクエストしないでください。デベロッパ向けのガイダンスは、[`ageAtLeast(_:)`](/documentation/ProximityReader/MobileDriversLicenseDataRequest/Element/ageAtLeast\(_:\))を参照してください。

**Apple Business Registerの条件を満たすアプリの場合、リクエストを行うときにユーザが組織についての重要な情報を表示できるように、ID確認に登録する。** Apple Business RegisterにID確認の登録を行うと、システムに正式な組織名とロゴを提供し、ユーザのデバイスのID確認UIの一部として表示できます。アプリが条件を満たすかどうか、および登録の方法については、[Apple Business Register](https://register.apple.com/services/login?returnTo=/signin/tap-to-present-id-on-iphone)を参照してください。

**確認プロセスを開始するボタンを提供する。** 単純な年齢チェックを行うボタンでは「年齢を確認」、さらに詳細な本人データをリクエストするボタンでは「本人であると確認」などのラベルを使用します。NFCやQRコードなど、特定の種類の通信を表す記号は含めないようにします。ボタンのラベルにAppleロゴを含めてはいけません。

ボタンのタイプ| 使用例  
---|---  
![「年齢を確認」ボタンの図。](https://docs-assets.developer.apple.com/published/68f99fdea3def2ba04aee092c3465400/id-verifier-button-age%402x.png)| ユーザがイベントに参加できる、またはコンサートホールなどの会場にアクセスできる年齢かどうかを確認するアプリ。  
![「本人であると確認」ボタンの図。](https://docs-assets.developer.apple.com/published/1e827d68149ef111a2ff7ebec21912a0/id-verifier-button-identity%402x.png)| レンタカーを借りるときに、名前や生年月日などの特定の身元情報が期待される値と一致するかどうかを確認するアプリ。  
  
**提示のみのリクエストでは、アプリのユーザが視覚的に確認を行う際にフィードバックを提供する。** 例えば、リーダーにユーザの肖像が提示される場合、アプリが応答の一部として承認または拒否の値を受け取ることができるように、「一致」および「不一致」のラベルが付いたボタンを提供します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/id-verifier#Platform-considerations)

 _iOSに追加の考慮事項はありません。iPadOS、macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/id-verifier#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/id-verifier#Related)

[Apple Business Register](https://register.apple.com/services/login?returnTo=/signin/tap-to-present-id-on-iphone)

[ウォレットの身分証明書](https://learn.wallet.apple/id)

[本人確認](/jp/design/human-interface-guidelines/wallet#Identity-verification)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/id-verifier#Developer-documentation)

[iPhoneアプリで確認APIを採用する](/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app) — ProximityReader

#### [ビデオ](/jp/design/human-interface-guidelines/id-verifier#Videos)

[](https://developer.apple.com/videos/play/wwdc2023/10114)

## [変更履歴](/jp/design/human-interface-guidelines/id-verifier#Change-log)

日付| 変更内容  
---|---  
2023年9月12日| 新規ページ。
