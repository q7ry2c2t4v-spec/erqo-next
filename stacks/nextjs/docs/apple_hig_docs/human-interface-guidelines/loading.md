# 読み込み

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/loading

# 読み込み

ユーザが気づく前にコンテンツを読み込み終わるのが、一番優れた体験です。

![回転する不確定的なアクティビティインジケータスケッチ。データの読み込みを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/cfdf824156ed794426ac55a2cb38ec15/patterns-loading-intro%402x.png)

アプリやゲームでアセット、レベル、その他のコンテンツを読み込む場合は、ユーザ体験を妨げたり、悪影響を与えないように動作を設計してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/loading#Best-practices)

**できるだけ早く表示する。** 読み込み完了まで何も表示されずに待たされると、ユーザはこのアプリやゲームで問題が起きているのではないかと思ってしまいます。このような状況では、コンテンツを読み込むときに、プレースホルダのテキスト、グラフィックス、アニメーションなどを表示し、コンテンツが利用できるようになるのにつれてこれらの要素を置き換えていくことを検討してください。

**アプリやゲームでコンテンツの読み込みを待つ間にほかのことを行えるようにする。** バックグラウンドでコンテンツを読み込むと、ユーザがほかのアクションを利用できるようになります。例えば、ゲームでバックグラウンドでコンテンツを読み込む間に、プレイヤーは次のレベルについて学んだり、ゲーム内メニューを確認したりできます。デベロッパ向けのガイダンスは、[大容量のダウンロードが必要なゲームでのプレイヤー体験を改善する](/documentation/GameKit/improving-the-player-experience-for-games-with-large-downloads)（英語）を参照してください。

**読み込みに長い時間がかかるのが避けられない場合はユーザが待っている間に何か有意義な視覚的コンテンツを提供する。** 例えば、ゲームプレイのヒントを提供する、ヒントを表示する、新機能を紹介するといったことができます。残りの読み込み時間をできるだけ正確に計測できれば、せっかく提供したプレースホルダのコンテンツをユーザが最後まで見られなかったり、同じコンテンツを何度も繰り返し再生したりといった事態を避けることができます。

**インストールと起動にかかる時間を短縮するため、バックグラウンドで大規模なアセットをダウンロードする。** アセットのダウンロードをスケジュールする[Background Assets](/documentation/BackgroundAssets)フレームワークの使用を検討してください。例えば、ゲームレベルパック、3Dキャラクターモデル、テクスチャなどのアセットを、インストール直後、アップデート時、または処理を妨げない他のタイミングでダウンロードするように設定できます。

## [進行状況の表示](/jp/design/human-interface-guidelines/loading#Showing-progress)

**コンテンツの読み込み中であること、および完了するまでの予想時間を明確に通知する。** コンテンツは即座に表示されるのが理想ですが、状況によっては読み込みに多少時間がかかります。 _進行状況インジケータ_ と呼ばれるシステムが提供するコンポーネントを使えば、読み込みが続いていることを通知できます。基本的に、読み込みにかかる時間が予測できる場合は、 _確定的な_ 進行状況インジケータを使います。そうでない場合は、 _不確定的な_ 進行状況インジケータを使います。ガイダンスは、[進行状況インジケータ](/jp/design/human-interface-guidelines/progress-indicators)を参照してください。

**ゲームでは、カスタムの読み込みビューの作成を検討する。** 標準の進行状況インジケータはほとんどのアプリで問題ありませんが、ゲームの雰囲気にそぐわない場合もあるでしょう。ゲームのスタイルに合ったカスタムのアニメーションや要素を使って、ユーザをもっと引き付けておけるような体験をデザインすることを検討してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/loading#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSに追加の考慮事項はありません。_

### [watchOS](/jp/design/human-interface-guidelines/loading#watchOS)

**watchOSでは読み込みインジケータの表示はできる限り回避する。** Apple Watchでは素早い操作感が期待されています。あくまでコンテンツを即座に表示するという目標を維持してください。ただし、コンテンツの読み込みにどうしても1、2秒かかる状況では、画面を空白にするよりは読み込みインジケータを表示すべきです。

## [リソース](/jp/design/human-interface-guidelines/loading#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/loading#Related)

[起動](/jp/design/human-interface-guidelines/launching)

[進行状況インジケータ](/jp/design/human-interface-guidelines/progress-indicators)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/loading#Developer-documentation)

[Background Assets](/documentation/BackgroundAssets)

#### [ビデオ](/jp/design/human-interface-guidelines/loading#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/325)

## [変更履歴](/jp/design/human-interface-guidelines/loading#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| バックグラウンドで大規模なアセットをダウンロードすることを反映するため、ダウンロードの保存に関するガイダンスを改訂。  
2024年6月10日| 進行状況の表示とダウンロードの保存についてのガイドラインを追加、ゲームのガイダンスを改善。
