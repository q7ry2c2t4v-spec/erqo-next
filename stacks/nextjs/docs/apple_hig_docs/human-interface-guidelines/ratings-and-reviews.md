# 評価およびレビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/ratings-and-reviews

# 評価およびレビュー

ユーザは通常、アプリやゲームをダウンロードする前に評価やレビューを確認します。

![半分塗りつぶされた星のスケッチ。好感度の評価を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/b1af4abf5589aa0b48f86494d3d52eef/patterns-ratings-and-reviews-intro%402x.png)

肯定的な評価やレビューを増やすには全体的な使用感を向上させるのが一番ですが、ユーザにフィードバックを求める適切なタイミングを選ぶことも大切です。アプリによって状況は異なりますが、例えば、ユーザがアプリを起動する回数や頻度、利用する機能の数、完了したタスクの数などを考慮に入れるとよいかもしれません。

アプリの評価はApp Storeでいつでもできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/ratings-and-reviews#Best-practices)

**評価を求めるのは、ユーザがアプリやゲームをある程度使用したあとにする。** 例えば、ユーザが何らかのゲームレベルや重要なタスクを完了したときにプロンプトを表示します。初回起動時やオンボーディング中は、ユーザがまだアプリの価値をよく理解していなく意見もまとまっていないため、評価を求めないようにしてください。ユーザがアプリを使用していないうちに評価を求められたという印象を与えると、否定的なフィードバックが残される可能性が高くなります。

![macOSでアプリやゲームを評価するためのメッセージが表示されたUIの図。](https://docs-assets.developer.apple.com/published/875dc840193b9171e6dd02422e2becfd/ratings-and-reviews-ios-alert%402x.png)

**タスクを実行したりゲームをプレイしているユーザの邪魔をしないようにする。** フィードバックの要求は、ユーザの操作を妨害したり、ユーザが負担に感じたりする場合があります。アプリやゲーム中で、評価を求められても煩わしいと思わない自然な小休止や停止のタイミングを探してください。

**ユーザにしつこく要求しない。** 評価を繰り返し要求すると、ユーザは不快に思い、アプリの感想にマイナスな影響を与えかねません。次回の要求まで少なくとも1～2週間空けて、ユーザがアプリをさらに使用するようになってからプロンプトを再表示することを検討してください。

**システムで提供されるプロンプトを優先する。** iOS、iPadOS、macOSでは、ユーザに負担をかけずに一貫した方法でアプリやゲームの評価やレビューを要求できます。アプリ体験の中でフィードバックを求めるのに適した場所を指定すると、システムによって以前のフィードバックが確認され、未入力だった場合は評価とレビューの書き込み（オプション）を求めるプロンプトがアプリ内で表示されます。ユーザはフィードバックを入力するか、1回のタップまたはクリックでプロンプトを閉じることができます。また、インストールしたすべてのアプリでこのようなプロンプトを表示しないように選択することもできます。プロンプトの表示は、アプリごとに365日間で3回までに自動的に制限されています。デベロッパ向けのガイダンスは、[`SKStoreReviewController`](/documentation/StoreKit/SKStoreReviewController)を参照してください。

**評価の集計をリセットするメリットと評価の数が少なく表示されることの潜在的なデメリットについて比較検討する。** アプリまたはゲームの新しいバージョンをリリースする際に、直前のリセット以降に受け取った個々の評価の集計をリセットできます。リセットすると、評価は最新バージョンに対するものであることを意味しますが、結果として評価の合計数が減り、それによりユーザがアプリをダウンロードする意欲を下げてしまうこともあります。デベロッパ向けのガイダンスは、[Appの評価概要のリセット](https://help.apple.com/app-store-connect/#/devfb7e87af8)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/ratings-and-reviews#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/ratings-and-reviews#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/ratings-and-reviews#Related)

[評価、レビュー、および回答](https://developer.apple.com/app-store/ratings-and-reviews/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/ratings-and-reviews#Developer-documentation)

[`SKStoreReviewController`](/documentation/StoreKit/SKStoreReviewController) — StoreKit

## [変更履歴](/jp/design/human-interface-guidelines/ratings-and-reviews#Change-log)

日付| 変更内容  
---|---  
2023年9月12日| アートワークを追加。
