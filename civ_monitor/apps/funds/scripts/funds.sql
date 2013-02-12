select i.symbol, f.symbol, f.description, f.country_id,
f.currency_id, fund_classification_id, fund_scheme_id, registration_date,
cl.code legal_id, open_ended, notes
from core_fund f, core_issuer i, core_fundclassification cl
where f.issuer_id = i.id
