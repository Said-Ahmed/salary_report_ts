import pytest
from utils.parser import parse_files


@pytest.fixture
def sample_csv_content():
    return """id,name,hours_worked,rate
1,Alice,160,50
2,Bob,150,40"""


@pytest.fixture
def tmp_csv_file(tmp_path, sample_csv_content):
    file_path = tmp_path / "employees.csv"
    file_path.write_text(sample_csv_content)
    return file_path


def test_parse_files_single_file(tmp_csv_file):
    """Тест: корректное чтение одного файла"""
    employees = parse_files([tmp_csv_file])
    assert len(employees) == 2
    assert employees[0]['name'] == 'Alice'
    assert employees[0]['hours_worked'] == 160
    assert employees[1]['rate'] == '40'


def test_parse_files_multiple_files(tmp_path, sample_csv_content):
    """Тест: чтение нескольких файлов"""
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    file1.write_text(sample_csv_content)
    file2.write_text("""id,name,hours_worked,rate\n3,Carol,170,60""")

    employees = parse_files([file1, file2])
    assert len(employees) == 3
    assert employees[2]['name'] == 'Carol'


def test_parse_files_nonexistent_file(capsys):
    """Тест: обработка несуществующего файла"""
    employees = parse_files(["/nonexistent/file.csv"])
    assert len(employees) == 0

    captured = capsys.readouterr()
    assert "Файл /nonexistent/file.csv не найден" in captured.out


def test_parse_files_empty_list():
    """Тест: пустой список файлов"""
    employees = parse_files([])
    assert employees == []


def test_parse_files_mixed_valid_and_invalid(tmp_path, sample_csv_content, capsys):
    """Тест: смесь корректных и некорректных файлов"""
    valid_file = tmp_path / "valid.csv"
    valid_file.write_text(sample_csv_content)

    employees = parse_files([valid_file, "/invalid/path.csv"])
    assert len(employees) == 2

    captured = capsys.readouterr()
    assert "Файл /invalid/path.csv не найден" in captured.out