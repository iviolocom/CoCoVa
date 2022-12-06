<div align="center">
  <div align="center">
    <b><font size="5">Hướng dẫn sử dụng MMDETECTION</font></b>
  </div>
  <div>&nbsp;</div>
</div>
</div>

<b>1. Giới thiệu thư mục con của mmdetection </b>
├── checkpoints
├── CITATION.cff
├── configs
├── data
├── demo
├── docker
├── docs
├── LICENSE
├── MANIFEST.in
├── mmdet
├── model-index.yml
├── pytest.ini
├── README_en-EN.md
├── README.md
├── README_zh-CN.md
├── requirements
├── requirements.txt
├── resources
├── setup.cfg
├── setup.py
├── tests
├── tools
└── tutorial_exps

Thư mục checkpoints để lưu model 

Thư mục data là thư mục để xử lý dữ liệu trước khi training

Sau khi dữ liệu được label bằng phần mềm labelme

Mở file /demo/LabeledData_Processing.ipynb

Thực hiện theo các bước trong file

mmdetection là bộ công cụ khá hoàn chỉnh khi bạn muốn train bất cứ một model nào nhiệm vụ của bạn là cài đặt dữ liệu (dataset) sao cho phù hợp với model
trong thư mục mmdet dataset

Hãy nhớ chỉnh dữ liệu trong file __init__.py
