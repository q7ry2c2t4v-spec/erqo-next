# 起動

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/launching

# 起動

スムーズな起動体験で、アプリやゲームをすぐに開始できるようにします。

![四角とその中の右上隅を指す矢印の形状のポインタのスケッチ。新しい状態への遷移を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/4bc136a9c65a90ce20c6aa38979c7584/patterns-launching-intro%402x.png)

起動は、アプリやゲームを開いたときに始まり、初回のダウンロードを含め、最初の画面の準備ができたときに終わります。起動が完了したときに、[オンボーディング](/jp/design/human-interface-guidelines/onboarding)体験を提供すると、ユーザにアプリやゲームの大まかな概要を把握してもらうことができます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/launching#Best-practices)

**即座に起動する。** ユーザは、アプリやゲームをすぐに操作したいと考えており、数秒も待っていられないという人もいます。

**プラットフォームの必要に応じて起動画面を用意する。** iOS、iPadOS、tvOSでは、アプリやゲームを開始した瞬間にシステムから起動画面が表示され、そのあとすぐにアプリの最初の画面に切り替わります。これは、処理が高速で快適に操作できるという印象を与えます。ガイダンスは、[起動画面](/jp/design/human-interface-guidelines/launching#Launch-screens)を参照してください。macOS、visionOS、watchOSでは、起動画面は必要ではありません。

**スプラッシュスクリーンが必要な場合は、オンボーディングフローの最初で表示することを検討する。** スプラッシュスクリーンは、ブランドなどの伝えるべき情報を簡潔に伝える美しいグラフィックスです。オンボーディング体験を提供しない場合は、起動完了後すぐにスプラッシュスクリーンを表示することができます。

**アプリが再起動後した場合は再起動前の状態から再開できるように状態を回復する。** 元の状態にたどり着くために、アプリやゲームでのそれまでの手順をユーザが再現しなくてはならないような設計にはしないでください。元の状態の細かい点に至るまで、できる限り回復してください。例えば、ユーザの最近の位置までビューをスクロールし、ユーザがアプリを離れた時と同じ状態のウインドウを同じ場所に表示します。

## [起動画面](/jp/design/human-interface-guidelines/launching#Launch-screens)

 _macOS、visionOS、watchOSには適用されません。_

**あまり凝った起動画面にはしない。** 起動画面はオンボーディング体験の一部でもスプラッシュスクリーンでもありません。また、芸術的表現のための場所でもありません。起動画面の唯一の役割は、アプリが素早く起動して即座に使えるようになるという印象をユーザに与えることです。

**起動画面のデザインはアプリやゲームの最初の画面とほぼ同じにする。** 起動完了時に表示される画面と違って見える要素を含めると、起動画面から最初の画面への切り替え時にユーザが違和感を覚える可能性があります。アプリやゲームで最初の画面に移行する前に無地の画面が表示される場合は、その無地の画面のみを表示する起動画面を作成してください。さらに、起動画面をデバイスの現在の画面の向きや見た目のモードに合わせることも大切です。

**最初の画面にテキストが含まれる場合でも、起動画面にはテキストを含めないようにする。** 起動画面のコンテンツは固定なので、表示したテキストはローカライズされません。

**広告には利用しない。** 起動画面は宣伝の場ではありません。スプラッシュスクリーンや「～について」ウインドウのように見える画面を作成しないでください。ロゴなどのブランディング要素は、それらがアプリの最初の画面にも継続して表示されるのでない限り含めてはなりません。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/launching#Platform-considerations)

 _macOS、watchOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/launching#iOS-iPadOS)

**適切な向きで起動する。** アプリやゲームが縦向きと横向きの両方に対応している場合は、デバイスの現在の向きに合わせて起動します。インターフェイスが1つの向きだけで動作する場合はその向きで起動し、ユーザが必要に応じてデバイスを回転させるようにします。横向きだけのインターフェイスの場合は、ユーザがデバイスを左回転/右回転のいずれで横向きにしても正しい向きで起動することを確認してください。ガイダンスは、[レイアウト](/jp/design/human-interface-guidelines/layout)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/launching#tvOS)

注意

tvOSのアプリで多く使われている[レイヤード画像](/jp/design/human-interface-guidelines/images#Layered-images)とは異なり、起動画面は静的です。

**ライブビューイングアプリでは、ユーザがアプリを起動したらすぐに自動再生することを検討する。** ユーザはTVを観るためにアプリを使用します。数秒間操作がなかったら、新しいまたは最近視聴したライブコンテンツの再生を開始することをおすすめします。ガイダンスは、[ライブビューイングアプリ](/jp/design/human-interface-guidelines/live-viewing-apps)を参照してください。

### [visionOS](/jp/design/human-interface-guidelines/launching#visionOS)

**完全イマーシブ型のアプリでも共有スペースで起動することを検討する。** 共有スペースでウインドウを開けば、アプリやゲームに関するコンテキストをより多く提供できるだけでなく、読み込みの時間も確保できます。また、完全なイマーシブ体験を開くためのコントロールを提示できます。特に、共有スペースで実行中のアプリがほかにもある場合には、フルスペースに移行するかどうかを自分で選べた方がありがたいと考えるのが一般的です。ガイダンスは[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/launching#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/launching#Related)

[オンボーディング](/jp/design/human-interface-guidelines/onboarding)

[読み込み](/jp/design/human-interface-guidelines/loading)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/launching#Developer-documentation)

[アプリの起動画面を指定する](/documentation/Xcode/specifying-your-apps-launch-screen) — Xcode

[アプリのローンチに対応する](/documentation/UIKit/responding-to-the-launch-of-your-app) — UIKit

#### [ビデオ](/jp/design/human-interface-guidelines/launching#Videos)

[](https://developer.apple.com/videos/play/wwdc2019/423)

[](https://developer.apple.com/videos/play/wwdc2017/816)

## [変更履歴](/jp/design/human-interface-guidelines/launching#Change-log)

日付| 変更内容  
---|---  
2024年6月10日| スプラッシュスクリーンの表示に関するガイダンスを追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
